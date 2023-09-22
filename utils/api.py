import requests


base_url = 'https://reqres.in'     #Базовая URL


class ReqresAPI:

    @staticmethod
    def get_list_users(page_key):
        url = f'{base_url}/api/users?page={page_key}'
        result_get = requests.get(url=url)
        return result_get


    @staticmethod
    def get_simple_user(user_id):
        url = f'{base_url}/api/users/{user_id}'
        result_get = requests.get(url=url)
        return result_get


    @staticmethod
    def get_list_unknown():
        url = base_url + '/api/unknown'
        result_get = requests.get(url=url)
        return result_get


    @staticmethod
    def get_single_unknown(unknown_id):
        url = f'{base_url}/api/unknown/{unknown_id}'
        result_get = requests.get(url=url)
        return result_get


    @staticmethod
    def create_user(body):
        url = base_url + '/api/users'
        result_post = requests.post(url=url, json=body)
        return result_post


    @staticmethod
    def update_by_put_user_info(user_id, body):
        url = f'{base_url}/api/users/{user_id}'
        result_put = requests.put(url=url, json=body)
        return result_put


    @staticmethod
    def update_by_patch_user_info(user_id, body):
        url = f'{base_url}/api/users/{user_id}'
        result_put = requests.patch(url=url, json=body)
        return result_put


    @staticmethod
    def delete_user(user_id):
        url = f'{base_url}/api/users/{user_id}'
        result_post = requests.delete(url=url)
        return result_post


    @staticmethod
    def register(body):
        url = base_url + '/api/register'
        result_post = requests.post(url=url, json=body)
        return result_post


    @staticmethod
    def loging(body):
        url = base_url + '/api/login'
        result_post = requests.post(url=url, json=body)
        return result_post


    @staticmethod
    def get_list_users_with_delay(delay):
        url = f'{base_url}/api/users?delay={delay}'
        result_get = requests.get(url=url)
        return result_get
