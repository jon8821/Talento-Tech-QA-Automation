from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(login_in_driver):
    try:
        driver = login_in_driver
        wait = WebDriverWait(driver, 10)

        # Esperar que los productos del inventario estén visibles
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        # Agregar el primer producto de la lista al carrito
        productos[0].find_element(By.TAG_NAME, "button").click()
        print('Se presiona el botón "Add to cart" del primer producto.')

        # Esperar a que aparezca el ícono del carrito con número (badge)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        assert carrito == "1", f"El número en el carrito no es correcto (valor actual: {carrito})"
        print(f"El carrito muestra número de producto agregado ({carrito}).")

        # Hacer clic en el carrito (abrirlo)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Se hace clic en el carrito de compras.")

        # Esperar a que cargue la página del carrito
        wait.until(EC.url_contains("/cart.html"))
        assert "/cart.html" in driver.current_url, "No se redirigió correctamente al carrito de compras."
        print("Se visualiza el carrito de compras de forma correcta.")

        # Verificar que haya productos en el carrito
        try:
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
            products_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
            assert len(products_in_cart) > 0, "No existen productos en el carrito"
        except Exception:
            raise AssertionError("No se encontraron productos en el carrito después de 10 segundos.")
        print("Se visualiza el producto en el carrito de compras de forma correcta.")

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
