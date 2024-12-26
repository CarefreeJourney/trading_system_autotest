from time import sleep

import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium import webdriver

from common.report_add_img import add_img_2_report
from common.tools import get_project_path,sep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self,driver):
        """使用错误的账号登录"""
        # driver = DriverConfig().driver_config()
        with allure.step("登录"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_2_report(driver,"登录")
        # # driver.get("http://192.168.254.140")
        # driver.get("http://www.tcpjwtester.top")
        # sleep(3)
        # LoginPage().login_input_value(driver,"用户名","周杰伦")
        # sleep(1)
        # LoginPage().login_input_value(driver,"密码","1234abcd!")
        # sleep(1)
        # LoginPage().click_login(driver,"登录")
        # sleep(3)
        # driver.quit()
"""
    def test_login2(self):
        # driver = DriverConfig().driver_config()
        driver = webdriver.Chrome(
            ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
                                latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                cache_manager=DriverCacheManager(valid_range=365)).install())
        driver.get("http://www.tcpjwtester.top")
        sleep(3)
        LoginPage().login_input_value(driver,"用户名","周杰伦")
        sleep(1)
        LoginPage().login_input_value(driver,"密码","1234abcd!")
        sleep(1)
        LoginPage().click_login(driver,"登录")
        sleep(3)
        driver.quit()

    def test_login3(self):
        # options=webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            executable_path=get_project_path()+sep(["driver_files",
                                                    "chromedriver"],add_sep_before=True)
        )
        driver.get("http://www.tcpjwtester.top")
        sleep(3)
        driver.quit()
"""