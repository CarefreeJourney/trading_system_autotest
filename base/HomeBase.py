# @Version：
# @Time：2024/12/8 22:00
# @Author：ChuliLin
# @Description：
class HomeBase:
    def wallet_switch(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'el-switch__core')]"

    def logo(self):
        """
        进入系统后，首页左上角的logo
        :return:
        """
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        首页，欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎')]"

    def show_date(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avator(self):
        """
        首页用户头像大图
        :return:
        """
        return "//span[starts-with(text(),'欢迎')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar2(self):
        """
        首页用户头像大图2，使用 ancestor
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"


