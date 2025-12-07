import requests
import pytest
import json
import time
from utils.logger import logger

@pytest.mark.api
@pytest.mark.reqres
def test_api_put_users(url_base,header_request):
    test = "Test API PUT"

    logger.info(f"Iniciando '{test}'")

    url = f"{url_base}/2"

    payload = {
        "name": "Loki",
        "job": "Dios de las travesuras"
    }
    
    logger.info(f"{test} - Enviando solicitud PUT para actualizar un usuario")
    inicio = time.time()
    response = requests.put(url, headers=header_request, json=payload)
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

    # VERIFICAR QUE EL NOMBRE Y EL TRABAJO SEAN CORRECTOS
    assert data["name"] == payload["name"], "El nombre no es correcto"
    assert data["job"] == payload["job"], "El trabajo no es correcto"
    logger.info(f'{test} - El nombre y el trabajo son correctos: {data["name"]}, {data["job"]}')
    #print("El nombre y el trabajo son correctos")

    # VERIFICAR QUE SE HAYA CREADO LA FECHA DE ACTUALIZACION
    assert "updatedAt" in data, "No se creo la fecha de actualizacion"
    logger.info(f'{test} - Se creo la fecha de actualización del usuario: {data["updatedAt"]}')
    #print(f'Fecha de actualización del usuario: {data["updatedAt"]}')

    