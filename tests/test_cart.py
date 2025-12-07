from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.saucedemo
@pytest.mark.cart
@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    test = "Test Cart - Parametrizado"
    try:
        driver = login_in_driver
        logger.info(f"Iniciando '{test}'")

        #Realizar el login
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"{test} - Ingresando usuario: {usuario} y contraseña: {password}")
        logger.info(f"{test} - Inicio de sesión exitoso")
        #print("Inicio de sesión exitoso")

        inventory_page = InventoryPage(driver)

        #Agregar al carrito el producto
        inventory_page.agregar_primer_producto()
        logger.info(f"{test} - Producto agregado al carrito")
        #print("Producto agregado al carrito")

        #Abrir el carrito
        inventory_page.abrir_carrito()
        logger.info(f"{test} - Abriendo el carrito")    
        #print("Se abre el carrito")

        #Validar el producto
        cartPage = CartPage(driver)

        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1, "El carrito tiene una cantidad de productos distinta a 1"
        logger.info(f"{test} - El carrito tiene 1 solo producto")
        #print("Se valida que el carrito tiene 1 producto")

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise