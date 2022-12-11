import pytest
from selenium.webdriver.common.by import By  # Для применения локаторов
from selenium import webdriver  # подключение библиотеки
from selenium.webdriver.support.ui import WebDriverWait  # Для применения явных ожиданий
from selenium.webdriver.support import expected_conditions as EC


def testing_all_pet_cards():
   '''Проверка всех карточек питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('D4559007@yandex.ru')

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('123456')

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   #Мы объявили три переменные, в которых записали все найденные элементы на странице:
   # в images — все картинки питомцев, в names — все их имена, в descriptions — все виды и возрасты
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''  # на странице нет питомцев без фото
      assert names[i].text != ''  # на странице нет питомцев без Имени
      assert descriptions[i].text != ''  # на странице нет питомцев с пустым полем для указания Породы и возраста
      assert ',' in descriptions[i].text  # проверяем, что между породой и лет есть запятая (значит есть оба значения)
      parts = descriptions[i].text.split(", ")  # Создаём список, где разделитель значений - запятая
      assert len(parts[0]) > 0  # Проверяем, что длина текста в первой части списка и
      assert len(parts[1]) > 0  # ...и во второй > 0, значит там что-то да указано! Если нет -> FAILED!