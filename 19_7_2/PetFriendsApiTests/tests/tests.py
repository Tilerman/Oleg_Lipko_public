# """Модуль 19"""
# import json
#
# import requests
# from settings import valid_email, valid_password
#
# class PetFriends:
#     """апи библиотека к веб приложению Pet Friends"""
#
#     def __init__(self):
#         #self.base_url = "https://petfriends1.herokuapp.com/"
#         self.base_url = 'https://petfriends.skillfactory.ru/'
#     def get_api_key(self, email: str, password: str) -> json:
#         """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
#         JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""
#
#         headers = {
#             'email': valid_email,
#             'password': valid_password,
#         }
#         res = requests.get(self.base_url, headers=headers)
#         status = res.status_code
#         result = ""
#         try:
#             result = res.json()
#         except json.decoder.JSONDecodeError:
#             result = res.text
#         #print(status, result)
#         return status, result
# result = ""
# base_url = "https://petfriends.skillfactory.ru/login"
# headers = {
#             'email': valid_email,
#             'password': valid_password,
#         }
# PetFriends.get_api_key('gogi@mail.ru', 'bab123')
# res = requests.get(base_url, headers = headers)
# status = res.status_code
# result = res.text
# print(status)
#print(result)

import requests
import pytests
from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

test_get_api_key_for_valid_user(email=valid_email, password=valid_password)
