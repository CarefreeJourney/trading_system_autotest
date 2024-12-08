# @Version：
# @Time：2024/10/10 16:58
# @Author：ChuliLin
# @Description：
from time import sleep

from config.driver_config_old import DriverConfig
driver = DriverConfig().driver_config()
driver.get("http://192.168.254.140")
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("1234abcd!")
sleep(1)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(3)
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.bilibili.com")
# driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys("软件测试老白")
# driver.find_element(By.CLASS_NAME,'nav-search-btn').click()
# time.sleep(3)
# driver.close()

