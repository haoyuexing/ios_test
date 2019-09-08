from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 列表特征
    list_button = By.XPATH, "//*[@name='列表']"

    # 百度特征
    baidu_button = By.XPATH, "//*[@name='百度']"

    # 点击列表
    def click_list(self):
        self.click(self.list_button)

    # 点击百度
    def click_baidu(self):
        self.click(self.baidu_button)