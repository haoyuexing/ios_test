import time

from base.base_driver import init_ios_driver
from base.base_page import Page


class TestScript:

    def setup(self):
        self.driver = init_ios_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_list(self):
        self.page.home.click_list()
        self.page.list.swipe_list()

    def test_baidu(self):
        self.page.home.click_baidu()
        self.page.baidu.input_keyword("hello")
        self.page.baidu.click_search()

        # 切换到网页
        # 1. 网页做事情
        # 2. 网页做事情
        # 3. 网页做事情
        # 4. 网页做事情
        # 切换到原生
        # 5. 原生做事情
        # 6. 原生做事情
        # 7. 原生做事情
        # 切换到网页
        # 8. 网页做事情
        # 9. 网页做事情
        # 10. 网页做事情

        # 15263478910
        # 切换到网页
        # 1. 网页做事情
        # 切换到原生
        # 5. 原生做事情
        # 切换到网页
        # 2. 网页做事情
        # 切换到原生
        # 6. 原生做事情
        # 切换到网页
        # 3. 网页做事情
        # 4. 网页做事情
        # 切换到原生
        # 7. 原生做事情
        # 切换到网页
        # 8. 网页做事情
        # 9. 网页做事情
        # 10. 网页做事情