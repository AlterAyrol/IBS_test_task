from utils.api import ReqresAPI
from utils.api_checking import Checking


class TestAPI:

    def test_get_list_users(self):
        body = {
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
        }
        result_get = ReqresAPI.get_list_users(2)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body)

    def test_get_simple_user(self):
        body = {
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
        }
        result_get = ReqresAPI.get_simple_user(2)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body)

    def test_get_single_user_not_found(self):
        body = {}
        result_get = ReqresAPI.get_simple_user(23)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_body(result_get, body=body)

    def test_get_list_unknown(self):
        body = {
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
}
        result_get = ReqresAPI.get_list_unknown()
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body)

    def test_get_list_resource(self):
        body = {
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
}
        result_get = ReqresAPI.get_list_unknown()
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body)

    def test_get_single_resource(self):
        body = {
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
}
        result_get = ReqresAPI.get_single_unknown(2)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body)

    def test_get_single_resource_not_found(self):
        body = {}
        result_get = ReqresAPI.get_single_unknown(23)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_body(result_get, body=body)

    def test_post_new_user(self):
        body_request = {
    "name": "morpheus",
    "job": "leader"
}
        body_response = ["name", "job", "id", "createdAt"]
        result_get = ReqresAPI.create_user(body_request)
        Checking.check_status_code(result_get, 201)
        Checking.check_json_key(result_get, expected_value=body_response)

    def test_put_update_user(self):
        body_request = {
    "name": "morpheus",
    "job": "zion resident"
}
        body_response = ["name", "job", "updatedAt"]
        result_get = ReqresAPI.update_by_put_user_info(2, body_request)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get, expected_value=body_response)

    def test_patch_update_user(self):
        body_request = {
            "name": "morpheus",
            "job": "zion resident"
        }
        body_response = ["name", "job", "updatedAt"]
        result_get = ReqresAPI.update_by_patch_user_info(2, body_request)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_key(result_get, expected_value=body_response)

    def test_delete_user(self):
        result_get = ReqresAPI.delete_user(2)
        Checking.check_status_code(result_get, 204)

    def test_register_successful(self):
        body_request = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
        body_response = {
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}
        result_get = ReqresAPI.register(body_request)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body_response)

    def test_register_unsuccessful(self):
        body_request = {
    "email": "sydney@fife"
}
        body_response = {
    "error": "Missing password"
}
        result_get = ReqresAPI.register(body_request)
        Checking.check_status_code(result_get, 400)
        Checking.check_json_body(result_get, body=body_response)

    def test_login_successful(self):
        body_request = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
        body_response = {
    "token": "QpwL5tke4Pnpja7X4"
}
        result_get = ReqresAPI.loging(body_request)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body_response)

    def test_login_unsuccessful(self):
        body_request = {
    "email": "peter@klaven"
}
        body_response = {
    "error": "Missing password"
}
        result_get = ReqresAPI.loging(body_request)
        Checking.check_status_code(result_get, 400)
        Checking.check_json_body(result_get, body=body_response)

    def test_delayed_response(self):
        body = {
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
}
        result_get = ReqresAPI.get_list_users_with_delay(3)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_body(result_get, body=body)
