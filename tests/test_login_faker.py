import pytest
from pages.login_page import LoginPage
from faker import Faker
from utils.logger import logger

#iniciamos Faker
fake = Faker()

@pytest.mark.saucedemo
@pytest.mark.login
@pytest.mark.parametrize("usuario,password,debe_funcionar", [
    (fake.user_name(),fake.password(),False),
    (fake.user_name(),fake.password(),False),
])
def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
    test = "Test Login con Faker"

    driver = login_in_driver
    logger.info(f"Iniciando '{test}'")

    logger.info(f"{test} - Probando con datos generados por el FAKER usuario: '{usuario}' y contraseña: '{password}'")
    #print(f"Probando con datos generados por el FAKER\nusuario: '{usuario}' y contraseña: '{password}'")
    
    #Realizar el login
    LoginPage(driver).login_completo(usuario,password)

    if debe_funcionar == True:
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario."
    else:
        mensaje_error = LoginPage(driver).obtener_error()
        #print(f"Mensaje de error recibido: {mensaje_error}")
        assert "Epic sadface" in mensaje_error, "No se mostró el mensaje de error esperado."
        logger.info(f"{test} - El login falló como se esperaba con el mensaje de error: {mensaje_error}")

