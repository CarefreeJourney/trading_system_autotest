# @Version：
# @Time：2024/12/31 16:42
# @Author：ChuliLin
# @Description：

from common.process_redis import Process
from common.ding_talk import send_dingtalk_msg_markdown
from common.qywx import send_qywx_msg_markdown
from common.yaml_config import GetConf

# 获取测试结果
total, success, fail, _ = Process().get_result()

# 拼接失败用例的名称
fail_testcases_name = "，失败的用例为："
msg_str = f"测试通过{str(success)}个，失败{str(fail)}个"
# 如果有失败的，就加上失败的用例名称
if int(fail) > 0:
    msg_str = msg_str + fail_testcases_name
    # 从 redis 中将失败的用例名称取出来
    fail_testcases_names = Process().get_fail_testcases_names()
    for i in range(len(fail_testcases_names)):
        if i == len(fail_testcases_names) - 1:
            fail_testcases_name += fail_testcases_names[i]
        else:
            fail_testcases_name += fail_testcases_names[i] + ","
        msg_str+=fail_testcases_names[i] + "\n"
else:
    fail_testcases_name = ""

# 插入测试结束时间
Process().write_end_time()
# 更改运行状态为零
Process().modify_running_status(0)

# 测试报告
# 项目名称
project_name = "trading_system_autotest"
# 报告标题
report_title = "UI自动化测试-测试报告"
# jenkins 地址
jenkins_url = GetConf().get_jenkins()["url"]
# allure 测试报告地址
allure_url=jenkins_url+"/job/"+project_name+"/allure/"
# 发送报告到钉钉
dingding_webhook = GetConf().get_dingding_webhook()
send_dingtalk_msg_markdown(
    dingding_webhook,
    allure_url,
    total,
    success,
    fail,
    fail_testcases_name,
    report_title
)
# 发送报告到企业微信
qywx_webhook = GetConf().get_qywx_webhook()
send_qywx_msg_markdown(
    qywx_webhook,
    allure_url,
    report_title,
    total,
    success,
    fail,
    fail_testcases_name
)