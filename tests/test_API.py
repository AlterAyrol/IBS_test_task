import requests
from utils.api import ReqresAPI
from utils.api_checking import Checking


class TestAPI:

    def test_get_list_users(self):
        result_get = ReqresAPI.get_list_users(2)
        Checking.check_status_code(result_get, 200)
        print(result_get.json())






