# @Version：
# @Time：2024/12/14 23:17
# @Author：ChuliLin
# @Description：

class GoodsBase:
    def goods_title(self):
        """
        商品标题
        :return:
        """
        return '//form[@class="el-form"]//textarea[@placeholder="请输入商品标题"]'
    def goods_details(self):
        """
        商品详情
        :return:
        """
        return '//form[@class="el-form"]//textarea[@placeholder="请输入商品详情"]'
    def goods_number(self,plus=True):
        """
        可以定位加号，也可以定位输入框
        :return:
        """
        if plus:
            return '//label[text()="商品数量"]/following-sibling::div//i[@class="el-icon-plus"]/parent::span'
        else:
            return '//label[text()="商品数量"]/following-sibling::div//input[@placeholder="商品数量"]'

    def goods_img(self):
        """
        商品图片
        :return:
        """
        return "//label[@for='product_detail_img']/following-sibling::div//div[@class='el-upload el-upload--picture-card']/input[@type='file']"

    def goods_price(self):
        """
        商品单价
        :return:
        """
        return "//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        商品状态
        :return:
        """
        return "//input[@placeholder='请选择商品状态']"

    def goods_status_select(self,select_name):
        """
        选择商品状态
        :param select_name:上架、下架
        :return:
        """
        return "//span[text()='"+select_name+"']/parent::li"

    def add_goods_bottom_button(self,button_name):
        """
        新增二手商品底部的按钮
        :param button_name:
        :return:
        """
        return "//span[text()='"+button_name+"']/parent::button"


