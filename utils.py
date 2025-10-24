from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)  # Espera máxima de 10 segundos

    # Esperar a que el campo de usuario sea visible y escribir
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    user_input.send_keys("standard_user")

    # Esperar a que el campo de contraseña sea visible y escribir
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")

    # Esperar a que el botón de login sea clickeable y hacer click
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
