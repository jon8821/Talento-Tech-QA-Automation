import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options

# Cada test abrirá y cerrará su propia instancia de Chrome
@pytest.fixture(scope="function")
def driver():
    chrome_opt = Options()
    # Abre Chrome en modo incógnito y evita ventanas emergentes molestas
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_in_driver(driver):
    # Inicia sesión antes de cada test
    login(driver)
    return driver
