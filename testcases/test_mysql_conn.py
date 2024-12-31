# @Version：
# @Time：2024/12/28 9:19
# @Author：ChuliLin
# @Description：
from time import sleep
import allure
from common.mysql_operate import MysqlOperate
from page.LoginPage import LoginPage
from page.HomePage import HomePage
from logs.log import log
class TestMysqlConn:
    def test_mysql(self,driver):
        """
        测试 mysql，判断账户余额和数据库是否一致
        """
        with allure.step("登录"):
            LoginPage().login(driver,"william")
            sleep(3)

        with allure.step("获取账户余额"):
            balance = HomePage().get_balance(driver)
            log.info(balance)

        with allure.step("从 mysql 中读取账户余额"):
            sql = "select balance from wallet where user_id=21"
            db_balance = MysqlOperate().query(sql) # ((Decimal('666'),),)
            db_balance = db_balance[0][0] # 取结果中第0个记录里面的第0个取出来的字段的值
            log.info(db_balance) # Decimal('666')

        with allure.step("断言数据库中的数据是否与页面数据一致"):
            assert str(balance) == str(db_balance)

