def test_login_validation(login_in_driver):

        print("Se inicia el navegador de forma correcta.")

        # Verificar que al ingresar credenciales redirija a productos
        assert "/inventory.html" in login_in_driver.current_url, "No se redirigió correctamente al inventario."
        print("Inicio de sesion correcto, se mostró la página principal de productos.")