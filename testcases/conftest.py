# @Version：
# @Time：2024/12/18 0:04
# @Author：ChuliLin
# @Description：
import pytest
from config.driver_config import DriverConfig

@pytest.fixture()
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()