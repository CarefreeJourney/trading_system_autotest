class LoginBase:
    def login_input(self,input_placeholder):
        """
        登录用户名、密码输入框
        :param input_placeholder:
        :return:
        """
        
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self,button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"

    def login_success(self):
        """
        登录成功
        :return:
        """
        return "//p[text()='登录成功']"

    def need_captcha(self):
        """
        是否需要验证码的单选框
        :return:
        """
        # return "//span[@class='el-checkbox__inner']"
        # 这样定位比较不会因为后期的改动而定位错误/定位不到
        return "//span[contains(text(),'是否需要验证码')]/preceding-sibling::span/span"

    def captcha(self):
        """
        验证码元素
        """
        return "//div[@class='el-image']/img"

    def input_captch(self):
        """
        输入验证码的输入框
        :return:
        """
        return "//input[contains(@placeholder,'请输入验证码')]"

# if __name__ == '__main__':
#     print(LoginBase().login_input("用户名"))
    # print(LoginBase().login_input("密码"))
    # print(LoginBase().login_button("登录"))