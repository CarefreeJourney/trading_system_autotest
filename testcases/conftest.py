# @Version：
# @Time：2024/12/18 0:04
# @Author：ChuliLin
# @Description：
import pytest
from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
@pytest.fixture()
def driver():
    global get_driver # 在函数内修改全局变量时，需要使用 global 关键字来避免局部变量的创建。
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item,call):# item 是用例
    # 内置钩子函数即回调函数， Java 中没有回调概念，但通过接口实现
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)

    if report.when == 'call':
        if report.failed:
            # 失败了就截图
            add_img_2_report(get_driver,"失败截图",need_sleep=False)
