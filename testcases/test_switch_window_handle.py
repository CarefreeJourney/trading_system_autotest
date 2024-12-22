# @Version：
# @Time：2024/12/15 16:47
# @Author：ChuliLin
# @Description：
from time import sleep
import allure
from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from common.report_add_img import add_img_2_report
class TestSwitchWindowHandle:
    @allure.description("窗口句柄")
    @allure.epic("窗口句柄 epic ")
    @allure.feature("窗口句柄 feature")
    @allure.story("窗口句柄 story")
    @allure.tag("窗口句柄 tag")
    def test_switch_window_handle(self,driver):
        # driver = DriverConfig().driver_config()
        with allure.step("登录"):
            LoginPage().login(driver,"jay")
            sleep(3)
            add_img_2_report(driver,"登录")
        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver,"外链")
            sleep(1)
            add_img_2_report(driver,"点击外链")
        with allure.step("断言 title"):
            title=ExternalLinkPage().goto_imooc(driver)
            print(title)
            assert title=="慕课网-程序员的梦工厂"
            # driver.quit()