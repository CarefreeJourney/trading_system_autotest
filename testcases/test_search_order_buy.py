# @Version：
# @Time：2024/12/15 17:17
# @Author：ChuliLin
# @Description：

from time import sleep
from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.OrderPage import OrderPage

class TestOrderBuy():
    def test_order_buy(self,driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver,"jay")
        LeftMenuPage().click_level_one_menu(driver,"我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"已买到的宝贝")
        sleep(2)
        tab_list=["全部","待付款","待发货","运输中","待确认","待评价"]
        for tab in tab_list: # tab_list 可做参数化，等到了 pytest 再说
            OrderPage().click_order_tab(driver,tab)
            sleep(2)
        # driver.quit()