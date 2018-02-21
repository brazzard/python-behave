from selenium.webdriver.common.by import By
from base_page import BasePage


class DetailPage(BasePage):

    def get_title(self):
        return self.browser.title
