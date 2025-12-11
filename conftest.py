import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import pathlib
import datetime as dt
import re

# Cada test abrirá y cerrará su propia instancia de Chrome
@pytest.fixture(scope="function")
def driver():
    chrome_opt = Options()

    chrome_opt.add_argument("--incognito") # Modo incógnito
    chrome_opt.add_argument("--no-sandbox") # Evita problemas de permisos en Linux
    chrome_opt.add_argument("--disable-gpu") # Deshabilita GPU
    chrome_opt.add_argument("--window-size=1920,1080") # Tamaño de ventana
    chrome_opt.add_argument("--headless=new") # Ejecutar sin interfaz gráfica
    chrome_opt.add_argument("--disable-extensions") # Deshabilitar extensiones
    
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()

# Cada vez que se ejecute un test, se abrirá la página de inicio de sesión
@pytest.fixture(scope="function")
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

# URL base para las pruebas de API
@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

# Headers para las peticiones de API
@pytest.fixture
def header_request():
    return {
        "x-api-key" : "reqres_fe7c78b9352645d6a4e0d451bf370738"
    }

# Función para capturar pantallas en caso de fallo

# Directorio donde se guardarán las capturas de pantalla
target = pathlib.Path("reports/screenshots")
# Crear carpeta si no existe
target.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when in ("setup", "call") and rep.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # Timestamp
            timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            # Convertir nombre del test a formato seguro
            test_name = re.sub(r'[^A-Za-z0-9_\-]', '_', item.name)
            # Generar nombre del archivo
            file_path = target / f"{rep.when}_{test_name}_{timestamp}.png"
            # Guardar captura