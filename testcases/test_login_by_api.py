# @Version：
# @Time：2024/12/27 17:37
# @Author：ChuliLin
# @Description：

from time import sleep
import pytest
import allure
from page.LoginPage import LoginPage

class TestLoginByApi:
    @pytest.mark.login
    @allure.feature("api登录")
    @allure.description("api登录")
    def test_login_by_api(self,driver):
        """
        api登录
        :return:
        """
        with allure.step("登录jay"):
            LoginPage().api_login(driver,"jay")
            sleep(5)

        with allure.step("切换用户到 william"):
            LoginPage().api_login(driver,"william")
            sleep(5)
