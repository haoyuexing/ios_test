from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class BaiduPage(BaseAction):

    keyword_edit_text = By.ID, "index-kw"

    search_button = By.ID, "index-bn"

    def input_keyword(self, text):
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.input(self.keyword_edit_text, text)
        self.driver.switch_to.context('NATIVE_APP')

    def click_search(self):
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.click(self.search_button)
        self.driver.switch_to.context('NATIVE_APP')

