import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class base_test(unittest.TestCase):

    # Iniciamos la prueba. SIEMPRE
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login1(self): # Ambos datos estan incorrectos
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        nombre = driver.find_element(By.ID, 'user-name')
        passw = driver.find_element(By.ID, 'password')
        btn = driver.find_element(By.ID, 'login-button')

        nombre.send_keys('Luana')
        passw.send_keys('adm123')
        btn.click()

        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        if (error == 'Epic sadface: Username and password do not match any user in this service'):
            print('El usuario y la contraseña son incorrectos. Prueba 1')

        time.sleep(3)

    def test_login2(self): # Falta el nombre
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        nombre = driver.find_element(By.ID, 'user-name')
        passw = driver.find_element(By.ID, 'password')
        btn = driver.find_element(By.ID, 'login-button')

        nombre.send_keys('')
        passw.send_keys('adm123')
        btn.click()

        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        if (error == 'Epic sadface: Username is required'):
            print('Falta el nombre. Prueba 2.')

        time.sleep(3)

    def test_login3(self): # Falta la contraseña
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        nombre = driver.find_element(By.ID, 'user-name')
        passw = driver.find_element(By.ID, 'password')
        btn = driver.find_element(By.ID, 'login-button')

        nombre.send_keys('Luana')
        passw.send_keys('')
        btn.click()

        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        if (error == 'Epic sadface: Password is required'):
            print('Falta la contraseña. Prueba 3')

        time.sleep(3)

    def test_login4(self): # Faltan ambos datos
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        nombre = driver.find_element(By.ID, 'user-name')
        passw = driver.find_element(By.ID, 'password')
        btn = driver.find_element(By.ID, 'login-button')

        nombre.send_keys('')
        passw.send_keys('')
        btn.click()

        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        if (error == 'Epic sadface: Username is required'):
            print('Faltan los datos. Prueba 4.')

        time.sleep(3)

    def test_login5(self): # Datos correctos
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        nombre = driver.find_element(By.ID, 'user-name')
        passw = driver.find_element(By.ID, 'password')
        btn = driver.find_element(By.ID, 'login-button')

        nombre.send_keys('standard_user')
        passw.send_keys('secret_sauce')
        btn.click()

        logo = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div')
        logo.is_displayed()
        print('El elemento es: ' + str(logo))
        print('Prueba 5')

        time.sleep(3)

    # Aqui cerramos la prueba. SIEMPRE
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

