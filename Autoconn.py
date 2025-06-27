from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NEU_NET():
    def __init__(self, url:str, username:str, password:str):
        self.url = url
        self.un = username
        self.pd = password

    def conn(self):
        # 创建一个Edge浏览器实例
        driver = webdriver.Edge()
        # 打开网址
        driver.get(self.url) # "http://ipgw.neu.edu.cn"

        # 等待页面加载
        time.sleep(1)

        try:
            button = driver.find_element_by_xpath("//button[text()='连接网络']")

            button.click()

            time.sleep(2)

            # 切换到登录页面
            driver.switch_to.window(driver.window_handles[-1])

            # 输入账户和密码
            username = driver.find_element_by_id("un")
            password = driver.find_element_by_id("pd")

            # 填写账户和密码，这里替换成你的账户和密码
            username.send_keys(self.un)
            password.send_keys(self.pd)

            # 提交登录
            password.send_keys(Keys.ENTER)

            # 等待登录完成
            time.sleep(2)
        except:
            time.sleep(0.5)
            

        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    url = "http://ipgw.neu.edu.cn"
    neu_id = "your id"
    neu_pd = "your password"

    neu_net = NEU_NET(url, neu_id, neu_pd)
    neu_net.conn()


