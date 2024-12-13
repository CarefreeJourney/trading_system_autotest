# @Version：
# @Time：2024/12/9 8:36
# @Author：ChuliLin
# @Description：
import time

from selenium.common.exceptions import ElementNotVisibleException,WebDriverException
from common.yaml_config import GetConf

class ObjectMap:
    # 获取基准地址
    url = GetConf().get_url()
    def element_get(self,driver,locate_type,locator_expression,timeout=10,must_be_visible=False): # 超时时间默认为10s
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible: 元素是否必须可见，True 必须可见
        :return: 返回元素
        """
        # 开始时间
        start_ms = time.time()*1000 # 单位为ms
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout*10)): # 100次，休眠0.1s，还没循环完的话，一定会超过10s
            # 查找元素
            try:
                element = driver.find_element(by=locate_type,value=locator_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须是可见的，则需要先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time()*1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式："+
                                         locate_type+"定位表达式"+
                                         locator_expression)

    def wait_for_ready_state_complete(self,driver,timeout=30):
        """
        等待页面完全加载完成
        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return:
        """
        # 开始时间
        # 时间换成毫秒级对比的意义是
        # 没有特殊的意义，仅仅只是为了防止减法出错，
        # time.time()获取到的是6位小数的数字，python中的运算是有精度问题的，
        # 整数位多，计算就更精确。
        start_ms = time.time()*1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout*10)):
            try:
                read_state=driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果 js 因为 driver 错误执行失败，就直接跳过
                time.sleep(0.03)
                return True
            if read_state == 'complete':
                # 为什么加休眠？在多浏览器并发跑的情况下，比如你的电脑CPU是6核，
                # 并发跑用例的时候，同时开启6个浏览器，因为chrome浏览器很占内存
                # 和CPU，服务器资源就会很快占满，这样浏览器特别容易崩溃，导致用例失败。
                # 所以适当的 sleep一点点，sleep哪怕0.01秒，都是对CPU、内存资源的合理利用。
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time()*1000
                # 如果超时，则break
                if now_ms >= stop_ms:
                    break
                # 配合for循环，乘以10的情况
                time.sleep(0.1)
        raise Exception("打开网页时，页面元素在%s秒后，仍然没有加载完成" % timeout)

    def element_disappear(self,driver,locate_type,locator_expression,timeout=30):
        """
        等待页面元素消失
        :param driver:浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression:定位表达式
        :param timeout: 超时时间
        :return:
        :notice: 可见和找不找得到是两回事，找得到未必可见，但是判断一个元素可不可见的前提必须得找到它.
        如果找不到，说明元素消失了（另一回事）
        """
        if locate_type: # 如果有传入定位方式
            # 开始时间
            start_ms = time.time()*1000
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout*10)):
                try:
                    element = driver.find_element(by=locate_type,value=locator_expression)
                    if element.is_displayed():
                        # 如果元素可见
                        now_ms = time.time()*1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1) # 元素还是没消失，继续循环
                except Exception:
                    # 没有获取到，说明消失了
                    return True
            raise Exception("元素没有消失，定位方式："+locate_type+"\n定位表达式:"+locator_expression)
        else:
            pass

    def element_appear(self,driver,locate_type,locator_expression,timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            start_ms = time.time()*1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout*10)):
                try:
                    element = driver.find_element(by=locate_type,value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time()*1000
                    if now_ms >= stop_ms:
                        break
                    # 没有找到
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("元素没有出现，定位方式"+locate_type+"定位表达式"+locator_expression)
        else:
            pass

    def element_to_url(self,
                       driver,
                       url,
                       locate_type_disappear=None,
                       locator_expression_disappear=None,
                       locate_type_appear=None,
                       locator_expression_appear=None,
    ):
        """
        跳转地址
        :param driver:
        :param url: 只需要传除了基准地址剩余的地址
        :param locate_type_disappear:
        :param locator_expression_disappear:
        :param locate_type_appear:
        :param locator_expression_appear:
        :return:
        :notice: 没有超时时间的参数
        """
        try:
            driver.get(self.url+url)
            # 等待页面元素都加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等待元素消失，加载完成后，元素不一定出现或者消失
            self.element_disappear(driver,
                                   locate_type_disappear,
                                   locator_expression_disappear
            )
            # 跳转地址后等待元素出现，加载完成后，元素不一定出现或者消失
            self.element_appear(driver,
                                locate_type_appear,
                                locator_expression_appear
            )
        except Exception as e: # try 中调用各种方法后出异常
            print("跳转地址出现异常，异常原因：%s" % e)
            return False
        return True # 没有异常，说明跳转地址成功

