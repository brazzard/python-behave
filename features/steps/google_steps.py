from selenium.webdriver.common.by import By
from behave import *
from page_objects.main_page import MainPage
from page_objects.search_results_page import SearchResultsPage
from page_objects.detail_page import DetailPage


@given('I am the user who opens the home page')
def step_impl(context):
    context.browser.get("https://www.google.com")


@when('I searches for keyword')
def step_impl(context):
    main_page = MainPage(context)
    main_page.perform_search("automation")


@step('I open first link')
def step_impl(context):
    search_result_page = SearchResultsPage(context)
    search_result_page.first_link()


@then('I should check page title')
def step_impl(context):
    detail_page = DetailPage(context)
    detail_page.get_title()
