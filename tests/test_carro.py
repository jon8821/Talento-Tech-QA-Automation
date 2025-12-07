from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import pytest
from utils.logger import logger

@pytest.mark.saucedemo
@pytest.mark.cart
def test_add_to_cart(login_in_driver):
    test = "Test Cart - No Paremetrizado"

    try:
        driver = login_in_driver
        wait = WebDriverWait(driver, 10)
        logger.info(f"Iniciando '{test}'")
        
        #Realizar el login
        usuario = "standard_user"
        password = "secret_sauce"
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"{test} - Ingresando usuario: {usuario} y contraseña: {password}")
        logger.info(f"{test} - Inicio de sesión exitoso")
        #print("Inicio de sesión exitoso")

        # Esperar que los productos del inventario estén visibles
        logger.info(f"{test} - Esperando que los productos del inventario estén visibles")
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        logger.info(f"{test} - Se encontraron {len(productos)} productos en el inventario")
        
        # Agregar el primer producto de la lista al carrito
        productos[0].find_element(By.TAG_NAME, "button").click()
        logger.info(f"{test} - Se presiona el botón 'Add to cart' del primer producto.")
        #print('Se presiona el botón "Add to cart" del primer producto.')

        # Esperar a que aparezca el ícono del carrito con número (badge)
        logger.info(f"{test} - Esperando que el ícono del carrito muestre el número de productos agregados")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1", f"El número en el carrito no es correcto (valor actual: {carrito})"
        logger.info(f"{test} - El carrito muestra número de producto agregado ({carrito}).")
        #print(f"El carrito muestra número de producto agregado ({carrito}).")

        # Hacer clic en el carrito (abrirlo)
        logger.info(f"{test} - Haciendo clic en el ícono del carrito para abrirlo")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        #print("Se hace clic en el carrito de compras.")

        # Esperar a que cargue la página del carrito
        logger.info(f"{test} - Esperando que cargue la página del carrito de compras")
        wait.until(EC.url_contains("/cart.html"))
        assert "/cart.html" in driver.current_url, "No se redirigió correctamente al carrito de compras."
        logger.info(f"{test} - Se redirige correctamente al carrito de compras.")
        #print("Se visualiza el carrito de compras de forma correcta.")

        # Verificar que haya productos en el carrito
        logger.info(f"{test} - Verificando que haya productos en el carrito de compras")
        try:
            logger.info(f"{test} - Esperando que los productos en el carrito estén visibles")
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
            products_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
            assert len(products_in_cart) > 0, "No existen productos en el carrito"
        except Exception:
            raise AssertionError("No se encontraron productos en el carrito después de 10 segundos.")
        logger.info(f"{test} - Se encontraron {len(products_in_cart)} productos en el carrito de compras.")
        #print("Se visualiza el producto en el carrito de compras de forma correcta.")

    except Exception as e:
        print(f"Error en test_carro: {e}")
        raise
