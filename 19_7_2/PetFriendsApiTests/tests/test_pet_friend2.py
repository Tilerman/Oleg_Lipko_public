from api import PetFriends
from settings import valid_email, valid_password, nonvalid_email, nonvalid_password
import os

pf = PetFriends()


def test_get_api_key_for_non_valid_email(email=nonvalid_email, password=valid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    #assert 'key' in result
    print(status)
    print(result)

def test_get_api_key_for_non_valid_password(email=valid_email, password=nonvalid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    #assert 'key' in result
    print(status)
    print(result)
def test_get_api_key_for_none_email(email='', password=valid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    #assert 'key' in result
    print(status)
    print(result)

def test_get_api_key_for_none_pasword(email=valid_email, password=''):
    """ Проверяем что запрос api ключа не возвращает статус 200 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    #assert 'key' in result
    print(status)
    print(result)

def test_get_api_key_for_non_valid_email_password(email=nonvalid_email, password=nonvalid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 Но тест дает ошибку,
    т.к. получилось зарегистрировать пользователя c ошибочным email - 123@123.12"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    #assert 'key' in result
    print(status)
    print(result)

def test_add_new_pet_with_non_valid_name(name=112, animal_type='ворона',
                                     age='5', pet_photo='images/8.jpg'):
    """Проверяем что нельзя добавить имя питомца как целое число 112"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
    assert result['name'] == name
    print(status)
    print(result)
def test_add_new_pet_with_non_valid_name2(name='112', animal_type='ворона',
                                     age='5', pet_photo='images/8.jpg'):
    """Проверяем что нельзя добавить имя питомца как строку число 112"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: удалось добавить питомца с именем '112'
    assert status != 200
    assert result['name'] == name
    print(status)
    print(result)

def test_add_new_pet_with_non_valid_age(name='Варвара', animal_type='ворона',
                                     age= 'a' , pet_photo='images/8.jpg'):
    """Проверяем что нельзя добавить возраст питомца как литерал 'а' """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: удалось присвоить питомцу буквенный возраст
    assert status != 200
    assert result['age'] == age
    print(status)
    print(result)
def test_add_new_pet_with_non_valid_age2(name='Варвара', animal_type='ворона',
                                     age= '20000' , pet_photo='images/8.jpg'):
    """Проверяем что нельзя добавить ,большой возраст питомца 20000 лет """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: удалось присвоить питомцу возраст 20000 лет
    assert status != 200
    assert result['age'] == age
    print(status)
    print(result)

def test_add_new_pet_with_non_valid_age3(name='Варвара', animal_type='ворона',
                                     age= 2, pet_photo='images/8.jpg'):
    """Проверяем что нельзя добавить возраст питомца как целое число 2 """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: не удалось присвоить питомцу возраст как целое 2
    assert status != 200
    assert result['age'] == age
    print(status)
    print(result)

def test_head_pet_info_with_valid_key():
    """ Проверяем метод head_pet_info """

    #_, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.head_pet_info()

    assert status == 200
    print(result)

def test_options_pet_info_with_valid_key():
    """ Проверяем метод options_pet_info """

    #_, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.options_pet_info()

    assert status == 200
    print(result)
