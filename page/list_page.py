import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ListPage(BaseAction):
    tenth_line = By.XPATH, "//*[@name='第 10 行']"
    fourth_line = By.XPATH, "//*[@name='第 4 行']"

    def swipe_list(self):
        print("----")
        # self.driver.swipe(100, 1000, 100, 100)

        # tenth_ele = self.find_element(self.tenth_line)
        # fourth_ele = self.find_element(self.fourth_line)
        #
        # self.driver.drag_and_drop(tenth_ele, fourth_ele)

        self.driver.execute_script("mobile: scroll", {"direction": "down"})
