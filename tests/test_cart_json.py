from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos
import time
from pages.login_page import LoginPage
from utils.logger import logger

RUTA_JSON = "datos/productos.json"

@pytest.mark.saucedemo
@pytest.mark.cart
@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    test = "Test Cart JSON"
    try:
        driver = login_in_driver
        logger.info(f"Iniciando '{test}'")

        #Realizar el login
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"{test} - Ingresando usuario: {usuario} y contraseña: {password}")
        logger.info(f"{test} - Inicio de sesión exitoso")
        #       print("Inicio de sesión exitoso")
        
        inventory_page = InventoryPage(driver)
        
        #Agregar al carrito los productos que estan en el json
        inventory_page.agregar_producto_por_nombre(nombre_producto)
        logger.info(f"{test} - Se agregó el producto '{nombre_producto}' al carrito.")
        #       print(f'Se agregó el producto "{nombre_producto}" al carrito.')
        
        #Abrir el carrito
        inventory_page.abrir_carrito()
        logger.info(f"{test} - Se abre el carrito de compras.")
        #        print("Se abre el carrito de compras.")

        #Validar el producto
        cartPage = CartPage(driver)
        
        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto
        logger.info(f"{test} - Se valida que el producto '{nombre_producto}' esté en el carrito de compras.")
        #        print(f'Se valida que el producto "{nombre_producto}" esté en el carrito de compras.')
        
        
    except Exception as e:
        print(f"Error en test_cart_json: {e}")
        raise