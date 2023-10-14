import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# ESTA ES LA PLANTILLA PARA LAS PRUEBAS CON UNITTEST.

class base_test(unittest.TestCase):

    # Iniciamos la prueba. SIEMPRE
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1(self):
        driver = self.driver
        driver.get('')
        time.sleep(2)


    # Aqui cerramos la prueba. SIEMPRE
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

