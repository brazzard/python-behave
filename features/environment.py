from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.implicitly_wait(2)


def after_all(context):
    context.browser.close()
