import requests
import pytest
import json
import time
from utils.logger import logger

@pytest.mark.api
@pytest.mark.reqres
def test_api_delete_users(url_base,header_request):

    test = "Test API DELETE"

    url = f"{url_base}/2"
    
    logger.info(f"Iniciando '{test}'")

    logger.info(f'{test} - Enviando solicitud DELETE a la URL: {url}')
    inicio = time.time()
    response = requests.delete(url, headers=header_request)
    fin = time.time()
    duracion = fin - inicio

    # VERIFICAR QUE SE HAYA REEMPLAZADO EL RECURSO
    assert response.status_code == 204, "El recurso no se creo correctamente"
    logger.info(f'{test} - Respuesta recibida con status code: {response.status_code}')
    #print(f'Status code: {response.status_code}')

    # VERIFICAR TIEMPO DE RESPUESTA
    assert duracion < 2, "El tiempo de respuesta es mayor a 2 segundos"
    logger.info(f'{test} - Tiempo de respuesta: {duracion} segundos')
    #print(f'Tiempo de respuesta: {duracion} segundos')
    