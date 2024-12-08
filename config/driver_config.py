
from selenium import webdriver

from common.tools import get_project_path, sep

class DriverConfig:
    def driver_config(self):
        options = webdriver.ChromeOptions()
        # 设置窗口大小
        options.add_argument("window-size=1920,1080")
        # 关闭左上角的 “chrome正受到自动测试软件的控制 ” 的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决 selenium 无法访问 https 的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略 localhost 上的 TLS/SSL 错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式，没有界面的情况下，不打开也可以运行自动化测试，在后台进行
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            executable_path=get_project_path() + sep(["driver_files", "chromedriver"], add_sep_before=True),
            options=options)
        # 删除所有 cookies
        driver.delete_all_cookies()
        return driver