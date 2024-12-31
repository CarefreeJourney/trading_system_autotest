# @Version：
# @Time：2024/12/18 0:04
# @Author：ChuliLin
# @Description：
import pytest
from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
from common.process_redis import Process
from common.yaml_config import GetConf
from common.ding_talk import send_dingtalk_msg
from logs.log import log
# 它允许你定义一些可复用的测试资源或环境设置，这些资源或环境可以在多个测试用例中共享
@pytest.fixture()
def driver():
    global get_driver # 在函数内修改全局变量时，需要使用 global 关键字来避免局部变量的创建。
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()

# 每个用例执行后会调用该法
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
            # add_img_2_report(get_driver,"失败截图",need_sleep=False)
            # 更新失败用例个数
            Process().update_fail()
            # 增加失败用例名称
            Process().insert_into_fail_testcase_names(report.description)
        elif report.passed:
            Process().update_success()
            # log.info("in pass~~~~~~~")
        else:
            pass
        process = Process().get_process()
        log.info("process为："+process)

        webhook = GetConf().get_dingding_webhook()
        send_dingtalk_msg(
            webhook,
            "测试用例："+report.description
            + "\n测试结果："
            + report.outcome
            + "\n自动化测试进度："
            + process,
        )


# 在所有用例执行前，统计好即将执行的用例总数后会调用该方法
def pytest_collection_finish(session): # pytest 内置的函数
    # 所有用例个数
    total = len(session.items)
    # 重置用例进度和失败用例名称
    Process().reset_all()
    # 初始化进度
    Process().init_process(total=total)