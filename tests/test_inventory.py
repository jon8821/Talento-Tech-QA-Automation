from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.saucedemo
@pytest.mark.inventory
@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    test = "Test Inventory - Parametrizado"
    try:
        driver = login_in_driver
        logger.info(f"Iniciando '{test}'")

        #Realizar el login
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"{test} - Ingresando usuario: {usuario} y contraseña: {password}")
        logger.info(f"{test} - Inicio de sesión exitoso")
        #print("Inicio de sesión exitoso")
        
        inventory_page = InventoryPage(driver)
        
        #Verificar que existan productos
        productos = inventory_page.obtener_todos_los_productos()
        assert len(productos) > 0, "El inventario esta vacio"
        logger.info(f"{test} - Cantidad de productos en inventario: {len(productos)}")
        #print(f"Cantidad de productos en inventario: {len(productos)}")
        
        #Verificar que el carrito este vacio al inicio
        assert inventory_page.obtener_conteo_carrito() == 0
        logger.info(f"{test} - El carrito esta vacio al inicio")
        #print("El carrito esta vacio al inicio")

        #Agregar el primer producto
        inventory_page.agregar_primer_producto()
        logger.info(f"{test} - Se agrego el primer producto al carrito")
        #print("Se agrego el primer producto al carrito")
        
        #Verificar el contador del carrito
        assert inventory_page.obtener_conteo_carrito() == 1
        logger.info(f"{test} - El contador del carrito se actualizo correctamente a 1")
        #print("El contador del carrito se actualizo correctamente a 1")
        
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise