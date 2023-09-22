import allure
from selene import browser
from selene import be, have


class StartPage:

    def __init__(self):
        self.browser = browser

    # Locators
    request_link_button_locator = '//div[@class="request"]//span'
    list_user_button_locator = 'data-key="endpoint"'
    single_user_button_locator = 'data-id="users-single"'
    users_single_not_found_button_locator = 'data-id="users-single-not-found"'
    unknown_list_button_locator = 'data-id="unknown"'
    unknown_single_button_locator = 'data - id = "unknown-single"'
    unknown_single_not_found_button_locator = 'data-id="unknown-single-not-found"'
    create_button_locator = 'data-id="post"'
    update_put_button_locator = 'data-id="put"'
    update_patch_button_locator = 'data-id="patch"'
    delete_button_locator = 'data-id="delete"'
    register_successful_button_locator = 'data-id="register-successful"'
    register_unsuccessful_button_locator = 'data-id="register-unsuccessful"'
    login_successful_button_locator = 'data-id="login-successful"'
    login_unsuccessful_button_locator = 'data-id="login-unsuccessful"'
    delayed_response_button_locator = 'data-id="delay"'


    # Actions

    @allure.step('открытие нужной страницы')
    def open_page(self, url):
        self.browser.open(url)

    @allure.step('Нажимаю на кнопку "Request"')
    def request_link_button_click(self):
        browser.element(self.request_link_button_locator).click()

    @allure.step('Нажимаю на кнопку "List users"')
    def list_user_button_click(self):
        browser.element(self.list_user_button_locator).click()

    @allure.step('Нажимаю на кнопку "Single user"')
    def single_user_button_click(self):
        browser.element(self.single_user_button_locator).click()

    @allure.step('Нажимаю на кнопку "Single user not found"')
    def users_single_not_found_button_click(self):
        browser.element(self.users_single_not_found_button_locator).click()

    @allure.step('Нажимаю на кнопку "List <resource>"')
    def unknown_list_button_click(self):
        browser.element(self.unknown_list_button_locator).click()

    @allure.step('Нажимаю на кнопку "Single <resource>"')
    def unknown_single_button_click(self):
        browser.element(self.unknown_single_button_locator).click()

    @allure.step('Нажимаю на кнопку "Single <resource> not found"')
    def unknown_single_not_found_button_click(self):
        browser.element(self.unknown_single_not_found_button_locator).click()

    @allure.step('Нажимаю на кнопку "Create"')
    def create_button_click(self):
        browser.element(self.create_button_locator).click()

    @allure.step('Нажимаю на кнопку "Update (Put)"')
    def update_put_button_click(self):
        browser.element(self.update_put_button_locator).click()

    @allure.step('Нажимаю на кнопку "Update (Patch)"')
    def update_patch_button_click(self):
        browser.element(self.update_patch_button_locator).click()

    @allure.step('Нажимаю на кнопку "Delete"')
    def delete_click(self):
        browser.element(self.delete_button_locator).click()

    @allure.step('Нажимаю на кнопку "Register - successful"')
    def register_successful_button_click(self):
        browser.element(self.register_successful_button_locator).click()

    @allure.step('Нажимаю на кнопку "Register - unsuccessful"')
    def register_unsuccessful_button_click(self):
        browser.element(self.register_unsuccessful_button_locator).click()

    @allure.step('Нажимаю на кнопку "Login - successful"')
    def login_successful_button_click(self):
        browser.element(self.login_successful_button_locator).click()

    @allure.step('Нажимаю на кнопку "Login - unsuccessful"')
    def login_unsuccessful_button_click(self):
        browser.element(self.login_unsuccessful_button_locator).click()

    @allure.step('Нажимаю на кнопку "Delayed response"')
    def login_unsuccessful_button_click(self):
        browser.element(self.delayed_response_button_locator).click()

    def current_url(self):
        browser.current_url


