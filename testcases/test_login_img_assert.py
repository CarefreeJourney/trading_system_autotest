# @Version：
# @Time：2024/12/21 18:23
# @Author：ChuliLin
# @Description：
from time import sleep
import pytest
from page.LoginPage import LoginPage
class TestLoginAssert:
    @pytest.mark.login
    def test_login_assert(self,driver):
        """
        登录后断言图片
        :param driver:
        :return:
        """
        LoginPage().login(driver,"jay")
        sleep(3)
        assert LoginPage().login_assert(driver,"head_img.png")>0.9

