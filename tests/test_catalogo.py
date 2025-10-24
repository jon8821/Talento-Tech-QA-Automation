from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_catalogo(login_in_driver):

    # Realiza el login
    driver = login_in_driver
    try:

        # Validar título de la página
        assert driver.title == "Swag Labs"
        print(f"El título de la pagina es: {driver.title}")

        #Verificar que existan productos dentro del catálogo
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No existen productos en la página"
        print(f"Existen {len(products)} productos en el catálogo")

        # Extrae el nombre del primer producto
        primer_producto = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert primer_producto == "Sauce Labs Backpack"
        # Extrae el precio del primer producto
        precio = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        assert precio == "$29.99"
        print(f'El nombre del primer producto es "{primer_producto}" con un valor de: {precio}')
    

        try:        
            # Buscar el botón del menú
            menu_button = driver.find_element(By.ID, "react-burger-menu-btn")

            # Verificar que esté visible
            assert menu_button.is_displayed(), "El botón de menú existe pero no está visible."
            print("El botón de menú está presente y visible.")

            # Si no existe el elemento ejecuta
        except NoSuchElementException:
            raise AssertionError("No se encontró el botón de menú en la página.")
        
        try:        
            # Buscar el botón del filtro
            filter_button = driver.find_element(By.CLASS_NAME, "product_sort_container")

            # Verificar que esté visible
            assert filter_button.is_displayed(), "El botón de filtro existe pero no está visible."
            print("El botón del filtro está presente y visible.")

            # Si no existe el elemento ejecuta
        except NoSuchElementException:
            raise AssertionError("No se encontró el botón del filtro en la página.")
        
    except Exception as e:
        print(f"Error en test_menu: {e}")
        raise
