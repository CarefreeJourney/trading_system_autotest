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
from tools import get_project_path,sep
from common.tools import get_project_path,sep
class GetConf:
    def __init__(self):
        # 获取 environment.yaml 的绝对路径，并打开 environment.yaml
        with open(get_project_path()+sep(["config","environment.yaml"],add_sep_before=True),
                  'r', encoding="utf-8") as file:
            self.env = yaml.load(file, Loader=yaml.FullLoader)

    def get_username_password(self):
        return self.env['username'], self.env['password']

if __name__ == '__main__':
    conf = GetConf()
    print(conf.get_username_password())