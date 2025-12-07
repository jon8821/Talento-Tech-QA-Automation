import requests
import pytest
import json
import time
from utils.logger import logger

@pytest.mark.api
@pytest.mark.reqres
def test_api_patch_users(url_base,header_request):
    test = "Test API PATCH"

    url = f"{url_base}/2"

    payload = {
        "name": "Heimdall"
    }
    
    logger.info(f"Iniciando '{test}'")

    logger.info(f'{test} - Enviando solicitud PATCH a la URL: {url}')
    inicio = time.time()
    response = requests.patch(url, headers=header_request, json=payload)
    fin = time.time()
    duracion = fin - inicio

    # VERIFICAR QUE SE HAYA REEMPLAZADO EL RECURSO
    assert response.status_code == 200, "El recurso no se creo correctamente"
    logger.info(f'{test} - Respuesta recibida con status code: {response.status_code}')
    #print(f'Status code: {response.status_code}')

    data = response.json()

    # Mostrar el JSON formateado
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # VERIFICAR TIEMPO DE RESPUESTA
    assert duracion < 2, "El tiempo de respuesta es mayor a 2 segundos"
    logger.info(f'{test} - Tiempo de respuesta: {duracion} segundos')
    #print(f'Tiempo de respuesta: {duracion} segundos')

    # VERIFICAR QUE EL NOMBRE ACTUALIZADO SEA CORRECTO
    assert data["name"] == payload["name"], "El nombre no es correcto"
    logger.info(f"{test} - El nombre se actualizó de forma correcta")
    #print("El nombre ese actualizó de forma correcta")

    # VERIFICAR QUE SE HAYA CREADO LA FECHA DE ACTUALIZACION
    assert "updatedAt" in data, "No se creo la fecha de actualizacion"
    logger.info(f'{test} - Fecha de actualización del usuario: {data["updatedAt"]}')
    #print(f'Fecha de actualización del usuario: {data["updatedAt"]}')

    