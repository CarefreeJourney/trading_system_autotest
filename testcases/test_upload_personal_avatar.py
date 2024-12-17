# @Version：
# @Time：2024/12/15 17:41
# @Author：ChuliLin
# @Description：

from time import sleep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.AccountPage import AccountPage
from page.LeftMenuPage import LeftMenuPage
class TestPersonalInfo:
    def test_upload_personal_avatar(self,driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver,"jay")
        LeftMenuPage().click_level_one_menu(driver,"账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver,"cg.jpg")
        sleep(3)
        AccountPage().click_save(driver)
        sleep(3)
        # driver.quit()