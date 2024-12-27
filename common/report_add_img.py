# @Version：
# @Time：2024/12/22 10:53
# @Author：ChuliLin
# @Description：
from time import sleep
import allure

def add_img_2_report(driver,step_name,need_sleep=True):
    """
    截图并插入 allure 报告
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    """
    if need_sleep:
        sleep(2)
    allure.attach(
        driver.get_screenshot_as_png(), # 直接截图并插入 allure 报告中
        step_name+".png",
        allure.attachment_type.PNG
    )

def add_img_path_2_report(img_path,step_name):
    """
    将图片插入 Allure 报告
    :param img_path:
    :param step_name:
    :return:
    """
    # 直接将截图好的图片作为附件插入 allure 报告，VS add_img_2_report 中的
    # allure.attach( driver.get_screenshot_as_png(),......)
    allure.attach.file(img_path,step_name,allure.attachment_type.PNG)

