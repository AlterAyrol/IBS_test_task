import allure
from allure_commons.types import Severity

from IBS_test_task.start_page import StartPage


class TestWEB:

    def test_list_user_button(self, web_browser):
        page = StartPage()

        page.request_link_button_locator()
        

