import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(autouse=True)
def testing(selenium):
    selenium = webdriver.Firefox()
    selenium.set_window_size(1920, 1080)
    selenium.maximize_window()


    yield

    selenium.quit()


def test_auth_valid_phone_valid_password(selenium):
    #переходим на сайт авторизации
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    #нажимаем кнопку выбора поля телефона
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода и вводим валидный номер мобильного телефона
    selenium.find_element(By.ID, 'username').clear()
    selenium.find_element(By.ID, 'username').send_keys('+79025105061')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    assert selenium.current_url.find('https://b2c.passport.rt.ru/account_b2c/page') != -1, "Mobil phone login error"
#
def test_auth_valid_email_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #time.sleep(30)

    #Нажимаем кнопку выбора ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим валидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    # Вводим валидный адрес Е-майл
    selenium.find_element(By.ID, 'username').send_keys('lipkoo@mail.ru')
    # Очищаем поле ввода и вводим валидный пароль

    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    assert selenium.current_url.find('https://b2c.passport.rt.ru/account_b2c/page') != -1, "E-mail login error"

def test_auth_valid_login_user_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-login")))
    #time.sleep(30)

    #Нажимаем кнопку выбора ввода логина пользователя
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    # Очищаем поле ввода и вводим валидный логин пользователя
    selenium.find_element(By.ID, 'username').clear()
    # Вводим валидный логин
    selenium.find_element(By.ID, 'username').send_keys('lk_22712971')
    #явное ожидание элемента поля пароля
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
     # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    assert selenium.current_url.find('https://b2c.passport.rt.ru/account_b2c/page') != -1, "Login user error"

def test_auth_valid_ls_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-ls")))
    #time.sleep(30)

    #Нажимаем кнопку выбора ввода логина пользователя
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    # Очищаем поле ввода и вводим валидный логин пользователя
    selenium.find_element(By.ID, 'username').clear()
    # Вводим валидный логин
    selenium.find_element(By.ID, 'username').send_keys('638010008669')
    #явное ожидание элемента поля пароля
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
     # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    assert selenium.current_url.find('https://b2c.passport.rt.ru/account_b2c/page') != -1, "Login ls error"

def test_auth_nonvalid_phone1_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода и вводим валидный номер мобильного телефона
    selenium.find_element(By.ID, 'username').clear()
    selenium.find_element(By.ID, 'username').send_keys('+79999999999')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(10)
    print("curent URL", selenium.current_url)
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone +79999999999 test error"

        #Ввод отрицательного числа вместо валидного номера телефона
def test_auth_nonvalid_phone2_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #Ввод отрицательного числа
    selenium.find_element(By.ID, 'username').send_keys('-79999999999')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    #time.sleep()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    #
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone -79999999999 test error"

    #ввод спецсимволов вместо валидного номера телефона
def test_auth_nonvalid_phone3_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #Ввод спецсимволов
    selenium.find_element(By.ID, 'username').send_keys('!"№;%:?*()')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    #time.sleep(10)
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    #
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number special symbol test error"

    #Ввод строчных кириллических символов вместо номера телефона
def test_auth_nonvalid_phone4_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #Ввод строчных кириллических символов
    selenium.find_element(By.ID, 'username').send_keys('эфывапролдж')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    #time.sleep(10)
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    #
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number small cyrilic test error"

   #Ввод заглавных кириллических символов вместо номера телефона
def test_auth_nonvalid_phone5_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #Ввод заглавных кириллических символов
    selenium.find_element(By.ID, 'username').send_keys('ЙЦУКЕНГШЩЗ')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    #
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number large cyrilic symbol test error"

   #Ввод строчных латинских символов вместо номера телефона
def test_auth_nonvalid_phone6_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)

    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #Ввод строчных кириллических символов
    selenium.find_element(By.ID, 'username').send_keys('asdfghjklpo')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()
    #time.sleep(10)
    print("curent URL", selenium.current_url)
    #
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number large latin symbol test error"

#Ввод заглавных латинских символов вместо номера телефона
def test_auth_nonvalid_phone7_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))

    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #Ввод заглавных кириллических символов
    selenium.find_element(By.ID, 'username').send_keys('ASDFGHJKLPO')
    # Очищаем поле ввода и вводим валидный пароль
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    #
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number large latin symbol test error"
    #Ввод 255 латинских символов A
def test_auth_nonvalid_phone8_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')

    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    str = 'A' * 255
    #Ввод 255 латинских символов 'A' через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number 255 latin symbol A test error"

    #Ввод 1000 латинских символов A
def test_auth_nonvalid_phone9_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')

    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    str = 'A' * 1000
    #Ввод 1000 латинских символов 'A' через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number 1000 latin symbol A test error"
    #Ввод 255 специальных символов '#'
def test_auth_nonvalid_phone10_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')

    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    str = '#' * 255
    #Ввод 255 латинских символов '#' через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number 255 latin symbol A test error"

    #Ввод 1000 специальных  символов '#'
def test_auth_nonvalid_phone11_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')

    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    str = '#' * 1000
    #Ввод 1000 специальных символов '#' через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number 1000 special symbol # test error"
    #Ввод 255 кирилических символов 'Й'
def test_auth_nonvalid_phone12_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')

    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    #заполняем строку str кириллической буквой 'Й'
    str = 'Й' * 255
    #Ввод 255 латинских символов '#' через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number 255 cyrilic symbol Й test error"

    #Ввод 1000 кириллических  символов 'Й'
def test_auth_nonvalid_phone13_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')

    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Очищаем поле ввода
    selenium.find_element(By.ID, 'username').clear()
    str = 'Й' * 1000
    #Ввод 1000 специальных символов '#' через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    #явное ожидание веб элемента
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')

    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.ID, 'kc-login').click()

    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "Mobil nonvalid phone number 1000 cyrilic symbol Й test error"
    #Ввод невалидного E-mail в правильном формате
def test_auth_nonvalid_email1_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #Нажимаем кнопку "Почта" выбора поля ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    # Вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').send_keys('bum123@mail.ru')
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "E-mail login bum123@mail.ru error"
    #Ввод невалидного E-mail в неправильном формате '123@4567.89'
def test_auth_nonvalid_email2_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #Нажимаем кнопку "Почта" выбора поля ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    # Вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').send_keys('123@4567.89')
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "E-mail login bum123@mail.ru error"

    #Ввод невалидного E-mail в неправильном формате 255 специальных символов '@'
def test_auth_nonvalid_email2_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #Нажимаем кнопку "Почта" выбора поля ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    #заполняем переменую  str 255 символами '@'
    str = '@' * 255
    # Вводим невалидный адрес Е-майл через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "E-mail login 255 symbol @ error"
    #Ввод невалидного E-mail в неправильном формате 1000 специальных символов '@'
def test_auth_nonvalid_email2_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #Нажимаем кнопку "Почта" выбора поля ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    #заполняем переменую  str 255 символами '@'
    str = '@' * 1000
    # Вводим невалидный адрес Е-майл через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "E-mail login 1000 symbol @ error"
   #Ввод невалидного E-mail в неправильном формате 255 цифр'1'
def test_auth_nonvalid_email3_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #Нажимаем кнопку "Почта" выбора поля ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    #заполняем переменую  str 255 символами '@'
    str = '1' * 255
    # Вводим невалидный адрес Е-майл через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)
    #Ввод невалидного E-mail в неправильном формате 1000 цифр'1'
    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "E-mail login 255 symbol 1 error"
    #Ввод невалидного E-mail в неправильном формате 1000 цифр '1'
def test_auth_nonvalid_email4_valid_password(selenium):
    selenium.get('https://b2c.passport.rt.ru/')
    #time.sleep(30)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    #Нажимаем кнопку "Почта" выбора поля ввода адреса E-mail
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # Очищаем поле ввода и вводим невалидный адрес Е-майл
    selenium.find_element(By.ID, 'username').clear()
    #заполняем переменую  str 255 символами '@'
    str = '1' * 1000
    # Вводим невалидный адрес Е-майл через переменную str
    selenium.find_element(By.ID, 'username').send_keys(str)
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    # Очищаем поле ввода и вводим валидный пароль
    selenium.find_element(By.ID, 'password').clear()
    selenium.find_element(By.ID, 'password').send_keys('Bambar3322!)')
    #time.sleep(30)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    selenium.find_element(By.ID, 'kc-login').click()
    #для контроля в случае непрохождения теста
    print("curent URL", selenium.current_url)

    assert selenium.current_url.find('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution') != -1, "E-mail login 1000 symbol 1 error"
