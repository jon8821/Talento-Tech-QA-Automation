# Proyecto de Automatización Web - Pre-Entrega Talento Tech QA Automation

Este proyecto forma parte de la Pre-Entrega del Curso de QA Automation con Python y Selenium.
El objetivo es demostrar la capacidad para automatizar flujos básicos de navegación web utilizando
Selenium WebDriver y Pytest sobre el sitio de práctica https://www.saucedemo.com.

---

## Propósito del Proyecto

Automatizar pruebas funcionales básicas sobre el sitio saucedemo.com, validando:
- Inicio de sesión exitoso con credenciales válidas.
- Navegación y verificación del catálogo de productos.
- Interacción con el carrito de compras (agregar y validar ítems).

---

## Tecnologías Utilizadas

- Python 3.12
- Pytest
- Selenium WebDriver
- Pytest-HTML (para reportes)
- Google Chrome / ChromeDriver

---

## Estructura del Proyecto

```txt
Talento-Tech-QA-Automation/
├── conftest.py # Configuración de fixtures de Selenium y login
├── run_tests.py # Script para ejecutar todos los tests y generar reporte HTML
├── utils.py # Funciones auxiliares (login, esperas, etc.)
├── tests/
│ ├── test_login.py # Validación de login exitoso
│ ├── test_catalogo.py # Verificación del catálogo y elementos de interfaz
│ └── test_cart.py # Prueba de agregar producto al carrito
└── reports/ # Carpeta donde se generan los reportes HTML
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
   pip install selenium pytest pytest-html
```
Asegurarse de tener instalado Google Chrome y ChromeDriver.
La versión de ChromeDriver debe coincidir con la versión del navegador Chrome.

---

## Ejecución de las Pruebas

Para ejecutar todas las pruebas y generar un reporte HTML automáticamente: 

```bash
   python run_tests.py
```
O bien, manualmente con Pytest:

```bash
   pytest -v --html=reports/reporte.html --self-contained-html
```
