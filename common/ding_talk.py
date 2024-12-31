# @Version：
# @Time：2024/12/31 14:11
# @Author：ChuliLin
# @Description：
import requests
from common.yaml_config import GetConf
from common.tools import get_every_wallpaper


def send_dingtalk_msg(webhook,content):
    """
    发送钉钉消息 - text
    :param webhook:
    :param content:
    :return:
    """
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    data={
        "msgtype": "text",
        "text":{
            "content": content,
            "at": {
                "isAtAll": False
            }
        }
    }
    res=requests.post(url=webhook,json=data,headers=headers)
    print("发送钉钉消息，返回结果：",res.text)

def send_dingtalk_msg_markdown(
        ding_webhook,
        allure_url,
        total_count,
        success_count,
        fail_count,
        failed_testcases_name,
        report_title
):
    """
    发送 markdown 格式的消息到钉钉
    :param ding_webhook:
    :param allure_url:
    :param total_count:
    :param success_count:
    :param fail_count:
    :param failed_testcases_name:
    :param report_title:
    :return:
    """
    # 获取壁纸
    wallpaper_url = get_every_wallpaper()
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    if fail_count == 0:
        failed_testcases_name = ""
    data={
        "msgtype": "markdown",
        "markdown":{
            "title": report_title,
            "text": "#### "
                + report_title
                + "\n >用例总数：{}个 \n > \n> 测试结果：通过{}个、失败{}个{} \n>   "
                  "![每日壁纸]({})\n> ###### 点击查看测试报告 \n> [Allure测试报告]({})".format(
                total_count,
                success_count,
                fail_count,
                failed_testcases_name,
                wallpaper_url,
                allure_url
            ),
        },
    }
    res=requests.post(url=ding_webhook,json=data,headers=headers)
    print("发送钉钉消息，返回结果：",res.text)


if __name__=='__main__':
    webhook = GetConf().get_dingding_webhook()
    send_dingtalk_msg(webhook,"lcl测试中")