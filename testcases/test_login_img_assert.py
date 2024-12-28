# @Version：
# @Time：2024/12/21 18:23
# @Author：ChuliLin
# @Description：
from time import sleep
import pytest
import allure
from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report
class TestLoginAssert:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self,driver):
        """
        登录后断言图片
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver,"jay")
            sleep(3)
        with allure.step("断言图片"):
            assert LoginPage().login_assert(driver,"head_img.png")>0.9

