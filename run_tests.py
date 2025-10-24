import pytest
import datetime
import os

# Crear carpeta "reports" si no existe
os.makedirs("reports", exist_ok=True)

# Generar nombre único según fecha y hora
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
report_name = f"report_{timestamp}.html"

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_catalogo.py",
    "tests/test_cart.py"    
]

# Argumentos para ejecutar pruebas: archivos + reporte html
pytest_args = test_files + [
    f"--html=reports/{report_name}",
    "--self-contained-html",
    "-v"
]

# Ejecutar pytest
pytest.main(pytest_args)

print(f"\n✅ Reporte generado: reports/{report_name}")
