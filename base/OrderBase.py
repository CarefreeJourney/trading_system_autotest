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

    def order_operation(self,product_title,operation):
        """
        订单的操作按钮
        :param product_title:
        :param operation:
        :return:
        """
        return "//div[text()='"+product_title+"']/parent::td/following-sibling::td[6]//span[text()='"+operation+"']/parent::button"

    def order_operation_confirm(self):
        """
        点击确认操作以后弹框的确定按钮
        :return:
        """
        return "//div[@class='el-dialog__wrapper' and contains(@style,'index')]//span[text()='确 定']/parent::button"
        # return "//span[text()='支付']/parent::div/following-sibling::div//span[text()='确 定']/parent::button" # 还有发货和确认收货都是
    def delivery_logistics(self):
        """
        发货的物流公司选择框
        :return:
        """
        return "//label[text()='物流公司']/following-sibling::div//input[@placeholder='请选择']/parent::div"

    def select_logistics(self,company):
        """
        物流公司
        :param company:
        :return:
        """
        return "//span[text()='"+company+"']/parent::li"

    def logistics_order_no(self):
        """
        物流单号
        :return:
        """
        return "//label[text()='物流单号']/following-sibling::div//input"

    def evaluation(self,num):
        """
        评价星级
        :param num:
        :return:
        """
        return "//span[text()='请给卖家评价']/following-sibling::div/span["+str(num)+"]/i"

    def evaluation_confirm(self):
        """
        评价完后确定
        :return:
        """
        # return "//div[contains(@style,'index')]//span[text()='确 定']/parent::button" # 由于之前点击了确认收货，因此定位有两个元素
        return "//span[text()='评价']/parent::div/following-sibling::div//span[text()='确 定']/parent::button"