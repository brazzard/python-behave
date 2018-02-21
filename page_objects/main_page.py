from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base_page import BasePage


class MainPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)
        self.context = context

    def search_field(self):
        return self.browser.find_element_by_name("q")

    def perform_search(self, search_word):
        q = self.search_field()
        q.send_keys(search_word)
        q.submit()
        WebDriverWait(self.browser, 10).until(
            ec.presence_of_element_located((By.ID, "resultStats")))