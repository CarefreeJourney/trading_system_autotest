# @Version：
# @Time：2024/10/25 20:53
# @Author：ChuliLin
# @Description：
# file = open("D:/dasi/test/"
#             "trading_system_autotest"
#             "/config/environment.yaml",
#             encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()
# with open("D:/dasi/test/"
#             "trading_system_autotest"
#             "/config/environment.yaml",
#              'r', encoding="utf-8") as file:
#     a = file.read()
#     print(a)
# with open("D:/dasi/test/"
#             "trading_system_autotest"
#             "/config/environment.yaml",
#              'r', encoding="utf-8") as file:
#     for a in file.readlines():
#         print(a)
import yaml
# from tools import get_project_path,sep
from common.tools import get_project_path,sep
class GetConf:
    def __init__(self):
        # 获取 environment.yaml 的绝对路径，并打开 environment.yaml
        with open(get_project_path()+sep(["config","environment.yaml"],add_sep_before=True),
                  'r', encoding="utf-8") as file:
            self.env = yaml.load(file, Loader=yaml.FullLoader)

    def get_username_password(self,user):
        # return self.env['username'], self.env['password']
        return self.env["user"][user]["username"],self.env["user"][user]["password"]
    def get_url(self):
        return self.env['url']

    def get_mysql_config(self):
        return self.env["mysql"]

    def get_redis(self):
        return self.env["redis"]

if __name__ == '__main__':
    print(GetConf().get_mysql_config())
#     conf = GetConf()
#     print(conf.get_username_password())