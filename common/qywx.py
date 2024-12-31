# @Version：
# @Time：2024/12/31 17:29
# @Author：ChuliLin
# @Description：

import requests

def send_qywx_msg_markdown(
        webhook,
        allure_url,
        report_title,
        total_count,
        success_count,
        fail_count,
        failed_testcases_name
):
    if fail_count==0:
        failed_testcases_name=""
    data={
        "msgtype":"markdown",
        "markdown": {
            # 企业微信的 markdown 不支持图片，因此不插入图片
            "content": "#### "
                    + report_title
                    + "\n >用例总数：{}个 \n >测试结果：通过{}个、失败{}个{} \n>   "
                      " ###### 点击查看测试报告 \n> [Allure测试报告]({})".format(
                total_count,
                success_count,
                fail_count,
                failed_testcases_name,
                allure_url
            ),
        },
    }
    res = requests.post(url=webhook,json=data)
    print(res.text)
    return True