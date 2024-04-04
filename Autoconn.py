## Main

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Edge浏览器实例
driver = webdriver.Edge()

# 打开网址
driver.get("http://ipgw.neu.edu.cn")

# 等待页面加载
time.sleep(2)

# 找到按钮并点击
button = driver.find_element_by_xpath("//button[text()='连接网络']")

button.click()

# 等待页面加载
time.sleep(2)

# 切换到登录页面
driver.switch_to.window(driver.window_handles[-1])

# 输入账户和密码
username = driver.find_element_by_id("un")
password = driver.find_element_by_id("pd")

# 填写账户和密码，这里替换成你的账户和密码
username.send_keys("your_username")
password.send_keys("your_password")

# 提交登录
password.send_keys(Keys.ENTER)

# 等待登录完成
time.sleep(2)

# 关闭浏览器
driver.quit()
