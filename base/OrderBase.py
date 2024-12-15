# @Version：
# @Time：2024/12/15 16:55
# @Author：ChuliLin
# @Description：

class OrderBase:
    def order_tab(self,tab_name):
        """
        订单 tab 按钮
        :param tab_name: 全部、待付款、待收货、运输中、待确认、待评价
        :return:
        """
        return "//div[@role='tab' and text()='"+tab_name+"']"

