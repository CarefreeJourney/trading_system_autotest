from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
# from common.tools import get_project_path, sep


class DriverConfig:
    def driver_config(self):
        option = webdriver.ChromeOptions()
        # 设置窗口大小
        option.add_argument("window-size=1920,1080")
        # 关闭左上角的 “chrome正受到自动测试软件的控制 ” 的提示
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决 selenium 无法访问 https 的问题
        option.add_argument("--ignore-certificate-errors")
        # 允许忽略 localhost 上的 TLS/SSL 错误
        option.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式，不要，否则报错：您之所以会看到此警告，是因为该网站不支持 HTTPS 且您处于无痕模式。
        # option.add_argument("--incognito")
        # 设置为无头模式，没有界面的情况下，不打开也可以运行自动化测试，在后台进行
        # options.add_argument("--headless")
        # 解决卡顿
        option.add_argument("--disable-gpu")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
                                latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                cache_manager=DriverCacheManager(valid_range=365)).install(),
            options=option)
        # 删除所有 cookies
        driver.delete_all_cookies()
        return driver
