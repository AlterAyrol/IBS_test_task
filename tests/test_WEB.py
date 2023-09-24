import allure
from allure_commons.types import Severity
import time
from IBS_test_task.start_page import StartPage


@allure.tag('WEB')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование WEB на главной странице')
class TestWEB:

    @allure.feature('WEB check list users')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'list users'. После переход по ссылке из поля 'Request'")
    def test_list_users_button(self, web_browser):
        body = '''{
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}'''

        browser = web_browser
        page = StartPage()

        page.list_user_button_click(browser)
        page.response_code_field_check(browser, status_code=200)

        page.response_body_field_check(browser, body=body)
        page.request_link_button_click(browser)

    @allure.feature('WEB check single user')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'single user'. После переход по ссылке из поля 'Request'")
    def test_get_single_user(self, web_browser):
        body = '''{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}'''

        browser = web_browser
        page = StartPage()

        page.single_user_button_click(browser)
        page.response_code_field_check(browser, status_code=200)

        page.response_body_field_check(browser, body=body)
        page.request_link_button_click(browser)

    @allure.feature('WEB check single user not found')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'single user not found'. После переход по ссылке из поля 'Request'")
    def test_single_user_not_found_button(self, web_browser):
        body = '{}'

        browser = web_browser
        page = StartPage()
        page.users_single_not_found_button_click(web_browser)
        page.response_code_field_check(browser, status_code=404)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check list <resource>')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'list <resource>'. После переход по ссылке из поля 'Request'")
    def test_get_list_unknown(self, web_browser):
        body = '''{
    "page": 1,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 1,
            "name": "cerulean",
            "year": 2000,
            "color": "#98B2D1",
            "pantone_value": "15-4020"
        },
        {
            "id": 2,
            "name": "fuchsia rose",
            "year": 2001,
            "color": "#C74375",
            "pantone_value": "17-2031"
        },
        {
            "id": 3,
            "name": "true red",
            "year": 2002,
            "color": "#BF1932",
            "pantone_value": "19-1664"
        },
        {
            "id": 4,
            "name": "aqua sky",
            "year": 2003,
            "color": "#7BC4C4",
            "pantone_value": "14-4811"
        },
        {
            "id": 5,
            "name": "tigerlily",
            "year": 2004,
            "color": "#E2583E",
            "pantone_value": "17-1456"
        },
        {
            "id": 6,
            "name": "blue turquoise",
            "year": 2005,
            "color": "#53B0AE",
            "pantone_value": "15-5217"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}'''

        browser = web_browser
        page = StartPage()
        page.unknown_list_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check single <resource>')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'single <resource>'. После переход по ссылке из поля 'Request'")
    def test_get_single_resource(self, web_browser):
        body = '''{
    "data": {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}'''

        browser = web_browser
        page = StartPage()
        page.unknown_single_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check single <resource> not found')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'single <resource> not found'. После переход по ссылке из поля 'Request'")
    def test_get_single_resource_not_found(self, web_browser):
        body = '{}'

        browser = web_browser
        page = StartPage()
        page.unknown_single_not_found_button_click(web_browser)
        page.response_code_field_check(browser, status_code=404)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check create')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'create'. После переход по ссылке из поля 'Request'")
    def test_post_new_user(self, web_browser):
        body = '''"name": "morpheus",
    "job": "leader",'''
        create_at = '"createdAt":'

        browser = web_browser
        page = StartPage()
        page.create_button_click(web_browser)
        page.response_code_field_check(browser, status_code=201)
        page.response_body_field_check(browser, body=body)
        page.response_body_field_check(browser, body=create_at)

        page.request_link_button_click(browser)

    @allure.feature('WEB check update (put)')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'update (put)'. После переход по ссылке из поля 'Request'")
    def test_put_update_user(self, web_browser):
        body = '''    "name": "morpheus",
    "job": "zion resident",'''
        update_at = '"updatedAt":'

        browser = web_browser
        page = StartPage()
        page.update_put_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)
        page.response_body_field_check(browser, body=update_at)

        page.request_link_button_click(browser)

    @allure.feature('WEB check update (patch)')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'update (patch)'. После переход по ссылке из поля 'Request'")
    def test_patch_update_user(self, web_browser):
        body = '''    "name": "morpheus",
    "job": "zion resident",'''
        update_at = '"updatedAt":'

        browser = web_browser
        page = StartPage()
        page.update_patch_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)
        page.response_body_field_check(browser, body=update_at)

        page.request_link_button_click(browser)
        time.sleep(1)

    @allure.feature('WEB check delete')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'delete'. После переход по ссылке из поля 'Request'")
    def test_delete_user(self, web_browser):
        body = ''

        browser = web_browser
        page = StartPage()
        page.delete_click(web_browser)
        page.response_code_field_check(browser, status_code=204)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check register successful')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'register successful'. После переход по ссылке из поля 'Request'")
    def test_register_successful(self, web_browser):
        body = '''{
    "id": 4,
    "token": '''

        browser = web_browser
        page = StartPage()
        page.register_successful_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check register unsuccessful')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'register unsuccessful'. После переход по ссылке из поля 'Request'")
    def test_register_unsuccessful(self, web_browser):
        body = '''{
    "error": "Missing password"
}'''

        browser = web_browser
        page = StartPage()
        page.register_unsuccessful_button_click(web_browser)
        page.response_code_field_check(browser, status_code=400)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check login successful')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'login successful'. После переход по ссылке из поля 'Request'")
    def test_login_successful(self, web_browser):
        body = '''{
    "token": "QpwL5tke4Pnpja7X4"
}'''

        browser = web_browser
        page = StartPage()
        page.login_successful_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check login unsuccessful')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'login unsuccessful'. После переход по ссылке из поля 'Request'")
    def test_login_unsuccessful(self, web_browser):
        body = '''{
    "error": "Missing password"
}'''

        browser = web_browser
        page = StartPage()
        page.login_unsuccessful_button_click(web_browser)
        page.response_code_field_check(browser, status_code=400)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

    @allure.feature('WEB check delayed response')
    @allure.story("Идёт проверка указанного статус кода и тела ответа в полях эталона при нажатии кнопки"
                  " 'delayed response'. После переход по ссылке из поля 'Request'")
    def test_delayed_response(self, web_browser):
        body = '''{
    "page": 1,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        {
            "id": 3,
            "email": "emma.wong@reqres.in",
            "first_name": "Emma",
            "last_name": "Wong",
            "avatar": "https://reqres.in/img/faces/3-image.jpg"
        },
        {
            "id": 4,
            "email": "eve.holt@reqres.in",
            "first_name": "Eve",
            "last_name": "Holt",
            "avatar": "https://reqres.in/img/faces/4-image.jpg"
        },
        {
            "id": 5,
            "email": "charles.morris@reqres.in",
            "first_name": "Charles",
            "last_name": "Morris",
            "avatar": "https://reqres.in/img/faces/5-image.jpg"
        },
        {
            "id": 6,
            "email": "tracey.ramos@reqres.in",
            "first_name": "Tracey",
            "last_name": "Ramos",
            "avatar": "https://reqres.in/img/faces/6-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}'''

        browser = web_browser
        page = StartPage()
        page.delayed_response_button_click(web_browser)
        page.response_code_field_check(browser, status_code=200)
        page.response_body_field_check(browser, body=body)

        page.request_link_button_click(browser)

