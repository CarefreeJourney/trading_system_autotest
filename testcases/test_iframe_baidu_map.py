# @Version：
# @Time：2024/12/15 17:58
# @Author：ChuliLin
# @Description：

from time import sleep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.IframeBaiduMapPage import IframeBaiduMapPage
from page.LeftMenuPage import LeftMenuPage
class TestIframeBaiduMap():
    def test_iframe_baidu_map(self,driver):
        """
        iframe 需要切换句柄
        :param driver:
        :return:
        """
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver,"jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver,"首页")
        sleep(3)
        # driver.quit()
