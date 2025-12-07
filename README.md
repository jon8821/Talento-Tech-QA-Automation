# Proyecto de Automatización Web - Pre-Entrega Talento Tech QA Automation

Este proyecto forma parte de la Entrega Final del Curso de QA Automation con Python y Selenium.
El objetivo es demostrar la capacidad para automatizar flujos de navegación web utilizando 
Selenium WebDriver y Pytest sobre el sitio de práctica https://www.saucedemo.com.

Aplicando practicas como Page Object Model, manejo de datos externos, generacion de reportes HTML,
logger y captura automatica de pantalla.

---

## Propósito del Proyecto

Automatizar pruebas de UI sobre el sitio [**saucedemo.com**](https://www.saucedemo.com) y de API sobre el sitio [**reqres.in**](https://reqres.in/api/users), validando:
- Inicio de sesión exitoso con credenciales válidas.
- Navegación y verificación del catálogo de productos.
- Interacción con el carrito de compras (agregar y validar ítems).
- Cobertura de diferentes métodos HTTP para API (GET, POST, PUT, PATCH Y DELETE)
- Generación de reportes, screenshots de errores y logs de las ejecuciones

---

## Tecnologías Utilizadas

- Python 3.XX
- Pytest
- Selenium WebDriver
- Pytest-HTML
- Google Chrome / ChromeDriver
- Logger
- Faker
- CSV / JSON
- Requests

---

## Estructura del Proyecto

```txt
Talento-Tech-QA-Automation/
├── conftest.py
├── run_tests.py
├── pytest.ini
├── utils/
│ ├── datos.py
│ ├── lector_json.py
│ ├── logger.py
├── pages/
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
├── datos/
│ ├── productos.json
│ ├── usuarios.csv
├── reports/
│ ├── screenshots/
│ │  ├── screenshot.png
│ ├── report.html
└── tests/
  ├── test_login.py
  ├── test_catalogo.py
  └── test_carro.py
  └── test_login_faker.py
  └── test_inventory.py
  └── test_cart.py
  └── test_cart_json.py
  └── test_api_get.py
  └── test_api_post.py
  └── test_api_put.py
  └── test_api_patch.py
  └── test_api_delete.py
  └── test_failed.py
```
---

## Instalación y Configuración

1. Clonar el repositorio:

```bash
   git clone https://github.com/jon8821/Talento-Tech-QA-Automation.git
   cd Talento-Tech-QA-Automation
```
Crear un entorno virtual (opcional pero recomendado):

```bash
   python -m venv venv
   venv\Scripts\activate     # En Windows
   source venv/bin/activate  # En macOS / Linux
```
Instalar dependencias:

```bash
   pip install selenium pytest pytest-html requests faker
```
Asegurarse de tener instalado Google Chrome y ChromeDriver.
La versión de ChromeDriver debe coincidir con la versión del navegador Chrome.

---

## Ejecución de las Pruebas

Para ejecutar todas las pruebas y generar un reporte HTML y log de ejecución automáticamente: 

```bash
   python run_tests.py
```
O bien, manualmente con Pytest:

```bash
   pytest -v --html=reports/reporte.html --self-contained-html
```
Al ejecutar `run_tests.py`, se crea la carpeta `logs` donde es creado el log de registro de la ejecución, por otra parte se crea también la carpeta `reports` y dentro de esta la carpeta `screenshots` donde:

El reporte es generado en la carpeta `reports` con formato HTML, el cual incluye:
 - Lista completa de test ejecutados
 - El estado de cada prueba
 - La duracion de cada test
 
 Mientras que las capturas de pantalla para pruebas fallidas se generan en la carpeta `screenshots` con formato PNG.

 ## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `usuarios.csv` --> datos de usuarios validos o invalidos
    - `productos.json` --> datos de productos para validación

## Conclusion
Este proyecto proporciona una estructura organizada, modular y escalable para la automatización de pruebas de API utilizando Python y Pytest. Incluye un flujo de ejecución simplificado mediante `run_tests.py`, junto con la generación automática de reportes HTML que facilitan el análisis y seguimiento de los resultados.

La arquitectura está diseñada para permitir la incorporación de nuevos casos de prueba y configuraciones sin necesidad de modificar el núcleo del framework. Esto garantiza buenas prácticas de mantenibilidad, favorece la reutilización del código y asegura que el proyecto pueda crecer de forma ordenada a lo largo del tiempo.