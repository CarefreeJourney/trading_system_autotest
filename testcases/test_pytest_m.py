# @Version：
# @Time：2024/12/16 22:22
# @Author：ChuliLin
# @Description：
from time import sleep
import pytest
from config.driver_config import DriverConfig
class TestPytestMClass:
    @pytest.mark.bing
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self):
        driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()

    @pytest.mark.antDesign
    def test_open_antDesign(self):
        driver = DriverConfig().driver_config()
        print("test_open_antDesign")
        driver.get("https://ant-design.antgroup.com/components/select-cn?locale=zh-CN")
        sleep(3)
        driver.quit()