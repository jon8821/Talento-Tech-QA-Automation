from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    # URL
    URL = "https://www.saucedemo.com/"

    # Locators
    _USER_INPUT = (By.ID, 'user-name')
    _PASS_INPUT = (By.ID, 'password')
    _LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def completar_user(self, usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    def completar_pass(self, password):
        input = self.driver.find_element(*self._PASS_INPUT)
        input.clear()
        input.send_keys(password)
        return self
    
    def hacer_clic_button(self):
        button = self.driver.find_element(*self._LOGIN_BUTTON)
        button.click()
        return self

    def login_completo(self, usuario, password):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_clic_button()
        return self
    
    def obtener_error(self):
        error_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3")))
        return error_element.text