from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
import pytest
from utils.logger import logger

@pytest.mark.saucedemo
@pytest.mark.inventory
def test_catalogo(login_in_driver):
    test = "Test Inventory - No Parametrizado"

    # Realiza el login
    driver = login_in_driver
    logger.info(f"Iniciando '{test}'")

    #Realizar el login
    usuario = "standard_user"
    password = "secret_sauce"
    LoginPage(driver).login_completo(usuario,password)
    logger.info(f"{test} - Ingresando usuario: {usuario} y contraseña: {password}")
    logger.info(f"{test} - Inicio de sesión exitoso")
    #print("Inicio de sesión exitoso")
    
    try:

        # Validar título de la página
        assert driver.title == "Swag Labs", f"El título de la página no es correcto. {driver.title} != Swag Labs"
        logger.info(f"{test} - El título de la página es correcto: {driver.title}") 
        #print(f"El título de la pagina es: {driver.title}")

        #Verificar que existan productos dentro del catálogo
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No existen productos en la página"
        logger.info(f"{test} - Existen {len(products)} productos en el catálogo")
        #print(f"Existen {len(products)} productos en el catálogo")

        # Extrae el nombre del primer producto
        primer_producto = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert primer_producto == "Sauce Labs Backpack", f"El nombre del primer producto no es correcto. {primer_producto} != Sauce Labs Backpack"
        # Extrae el precio del primer producto
        precio = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        assert precio == "$29.99", f"El precio del primer producto no es correcto. {precio} != $29.99"
        logger.info(f'{test} - El nombre del primer producto es "{primer_producto}" con un valor de: {precio}')
        #print(f'El nombre del primer producto es "{primer_producto}" con un valor de: {precio}')
    

        try:        
            # Buscar el botón del menú
            menu_button = driver.find_element(By.ID, "react-burger-menu-btn")

            # Verificar que esté visible
            assert menu_button.is_displayed(), "El botón de menú existe pero no está visible."
            logger.info(f"{test} - El botón de menú está presente y visible.")
            #print("El botón de menú está presente y visible.")

            # Si no existe el elemento ejecuta
        except NoSuchElementException:
            raise AssertionError("No se encontró el botón de menú en la página.")
        
        try:        
            # Buscar el botón del filtro
            filter_button = driver.find_element(By.CLASS_NAME, "product_sort_container")

            # Verificar que esté visible
            assert filter_button.is_displayed(), "El botón de filtro existe pero no está visible."
            logger.info(f"{test} - El botón de filtro está presente y visible.")
            #print("El botón del filtro está presente y visible.")

            # Si no existe el elemento ejecuta
        except NoSuchElementException:
            raise AssertionError("No se encontró el botón del filtro en la página.")
        
    except Exception as e:
        print(f"Error en test_catalogo: {e}")
        raise
