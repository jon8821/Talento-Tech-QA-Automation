from utils.logger import logger

def test_error_demo(driver):

    test = "Test Fallido"

    logger.info(f"Iniciando '{test}'")
    logger.info(f"{test} - Forzando error en codigo.")
    logger.info(f"{test} - Finalizado exitosamente.")
    assert False, "Probando un fallo intencional en el test para generar reporte, log y captura de pantalla."
