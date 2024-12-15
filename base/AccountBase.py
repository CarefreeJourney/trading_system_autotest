# @Version：
# @Time：2024/12/15 17:29
# @Author：ChuliLin
# @Description：
class AccountBase:
    def basic_info_avator_input(self):
        """
        基本资料-个人头像
        :return:
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        基本资料-保存按钮
        :return:
        """
        return "//span[text()='保存']/parent::button"