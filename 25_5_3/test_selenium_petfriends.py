import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_my_petfriends(web_browser):

    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH, '//html/body/div/div/div[2]/button')

    btn_newuser.click()
    time.sleep(5)
    # click existing user button
    btn_exist_acc = web_browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    btn_exist_acc.click()


    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("gogi@mail.ru")

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("bab123")
    # click submit button
    btn_submit = web_browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
 #web_browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn_submit.click()
    web_browser.find_element(By.CSS_SELECTOR, 'li.nav-item:nth-child(1) > a:nth-child(1)').click()
    text = web_browser.find_element(By.TAG_NAME, 'h2').text

    assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/my_pets',"login error"

    #print("text", text)
def test_amount_image_more_50_percent(selenium):
    selenium.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
    selenium.find_element(By.ID, 'email').send_keys('gogi@mail.ru')
   #pytest.driver.find_element_by_id('email').send_keys('gogi@mail.ru')
   # Вводим пароль
    selenium.find_element(By.ID, 'pass').send_keys('bab123')
   # Нажимаем на кнопку входа в аккаунт
   #pytest.driver.find_element(By.CSS_SELEKTOR, 'button[type="submit"]').click()
    btn_submit = selenium.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn_submit.click()

   # Проверяем, что мы оказались на главной странице пользователя
   #time.sleep(10)
    allpets = selenium.find_element(By.TAG_NAME, "h1")
    assert allpets.text == "PetFriends"

    mypets = selenium.find_element(By.CSS_SELECTOR, 'li.nav-item:nth-child(1) > a:nth-child(1)')
    mypets.click()

    mypets1 = selenium.find_element(By.CSS_SELECTOR, "body > div.task2.fill > div > div.\\.col-sm-4.left > h2")
    selenium.implicitly_wait(5)
    my_pet_amount_all = selenium.find_element(By.CSS_SELECTOR, "body > div.task2.fill > div > div.\\.col-sm-4.left")
    selenium.implicitly_wait(5)
    my_pet_amount_img = selenium.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > th > img')
    #Определение количества моих питомцев, указаное на странице
    index1 = my_pet_amount_all.text.find("в:", 10,14)
    index2 = my_pet_amount_all.text.find("Друзей:")
    index1 = index1+2
    index2 = index2-1
    str=""
    for num in range(index1, index2):
        #print("index1", index1, index2)
        str = str + my_pet_amount_all.text[num]
    number_my_pet = int(str)
    print("number_my_pet", number_my_pet)
    print("len my_pet_amount_img", len(my_pet_amount_img))
    #Считаем количество картинок в карточках и сумируем их в переменую number_images
    number_images = 0
    for i in range(len(my_pet_amount_img)):
        if len(my_pet_amount_img[i].get_attribute('src')) >= 1:
            number_images = number_images + 1
    quantity = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
    print(len(quantity))
    #проверяем процентное отношение количества имеющихся картинок к общему количеству моих питомцев
    assert number_images/number_my_pet >= 0.5, "Amount images less, then 50%"


def test_my_pets_have_name_type_age(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH, '//html/body/div/div/div[2]/button')

    btn_newuser.click()
    time.sleep(5)
    # click existing user button
    btn_exist_acc = web_browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    btn_exist_acc.click()


    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("gogi@mail.ru")

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("bab123")
    # click submit button
    btn_submit = web_browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    #Нажатие кнопки войти
    btn_submit.click()
    #вход на страницу Мои питомцы
    web_browser.find_element(By.CSS_SELECTOR, 'li.nav-item:nth-child(1) > a:nth-child(1)').click()
    #неявное ожидание
    web_browser.implicitly_wait(5)
    my_pet_amount_name = web_browser.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')
    # my_pet_amount_type = web_browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    # my_pet_amount_age = web_browser.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')
    #my_pet_amount1 = list(map(int, re.compile(r'(?<=Питомцев: )\d+').findall(my_pet_amount)))
    str1 = '//*[@id="all_my_pets"]/table/tbody/tr['
    str2 = ']/td['
    names = []
    # выполнение цикла для поиска имен, породы и возраста во всех карточках моих питомцев
    for i in range(1,len(my_pet_amount_name)+1):
        #print(str1+ str(i))
        #создание переменных локаторов
        locator1 = str1+ str(i)+ str2 +'1]'
        locator2 = str1+ str(i)+ str2 +'2]'
        locator3 = str1+ str(i)+ str2 +'3]'
        #print('locator1', locator1)
        web_browser.implicitly_wait(5)
        my_pet_amount_name = web_browser.find_element(By.XPATH, locator1)
        #создание списка имен для последующей проверки повторяющихся имен
        names.append(my_pet_amount_name.get_attribute('innerText'))
        #print("names", names)
        #проверка пустых полей имени питомца
        assert my_pet_amount_name.get_attribute('innerText') != "", "name is empty"
        web_browser.implicitly_wait(5)
        my_pet_amount_type = web_browser.find_element(By.XPATH, locator2)
        #проверка пустых полей породы питомца
        assert my_pet_amount_type.get_attribute('innerText')!= "", "type is empty"
        web_browser.implicitly_wait(5)
        my_pet_amount_age = web_browser.find_element(By.XPATH, locator3)
        #проверка пустых полей возраста питомца
        assert my_pet_amount_age.get_attribute('innerText') != "", "age is empty "

    # проверка отсутствия одинаковых имен питомцев
    for n in range(len(names)):
        assert names.count(names[n]) == 1, "equal name"


