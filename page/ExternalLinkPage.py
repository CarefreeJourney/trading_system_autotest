# @Version：
# @Time：2024/12/15 16:45
# @Author：ChuliLin
# @Description：
from base.ObjectMap import ObjectMap
class ExternalLinkPage(ObjectMap):
    def goto_imooc(self,driver):
        """
        切换窗口为慕课网
        :param driver:
        :return:
        """
        self.switch_window_2_latest_handle(driver)
        return driver.title