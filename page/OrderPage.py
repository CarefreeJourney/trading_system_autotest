# @Version：
# @Time：2024/12/15 17:13
# @Author：ChuliLin
# @Description：
from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase
from selenium.webdriver.common.by import By
class OrderPage(OrderBase,ObjectMap):
    def click_order_tab(self,driver,tab_name):
        """
        点击订单 tab 栏按钮
        :param driver:
        :param tab_name:
        :return:
        """
        tab_xpath=self.order_tab(tab_name)
        return self.element_click(driver,
                                  By.XPATH
                                  ,tab_xpath)

