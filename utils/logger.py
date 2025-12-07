import logging
import pathlib
import datetime

# Crear directorio de logs
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

# Nombre de archivo con timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
log_file = audit_dir / f'log_{timestamp}.log'

# Crear logger
logger = logging.getLogger("TalentoTech")
logger.setLevel(logging.INFO)

# Evitar duplicación de handlers
if not logger.handlers:

    # Handler para archivo
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")

    # Handler para consola
    console_handler = logging.StreamHandler()

    # Formato
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Asignar formato a los handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Agregar handlers al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
