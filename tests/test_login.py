import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_users
from utils.logger import logger

@pytest.mark.saucedemo
@pytest.mark.login
@pytest.mark.parametrize('usuario,password,debe_funcionar',leer_csv_users('datos/usuarios.csv'))

def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
        test = "Test Login CSV"

        
        driver = login_in_driver
        logger.info(f"Iniciando '{test}'")
        
        #Realizar el login
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"{test} - Realizando login con usuario: '{usuario}' y contraseña: '{password}'")
        #print(f"Probando con usuario: '{usuario}' y contraseña: '{password}'")

        # Verificar que al ingresar credenciales redirija a productos
        logger.info(f"{test} - Validando usuario y contraseña.")
        if debe_funcionar == True:
                logger.info(f"{test} - Verificando redirección a la página de inventario.")
                assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario."
                #print("Inicio de sesion correcto, se mostró la página principal de productos.")
                logger.info(f"{test} - Finalizada la prueba de login con credenciales válidas de forma exitosa.")
        else:
                mensaje_error = LoginPage(driver).obtener_error()
                logger.info(f"{test} - Verificando mensaje de error por credenciales inválidas.")
                #print(f"Mensaje de error recibido: {mensaje_error}")
                assert "Epic sadface" in mensaje_error, "No se mostró el mensaje de error esperado."
                logger.info(f"{test} - validando mensaje de error recibido: {mensaje_error}")
                logger.info(f"{test} - Finalizada la prueba de login con credenciales inválidas de forma exitosa.")