import requests
import pytest
import json
from utils.logger import logger

@pytest.mark.api
@pytest.mark.reqres
def test_api_post_users(url_base,header_request):
    test = "Test API POST"

    logger.info(f"Iniciando '{test}'")

    payload = {
        "name": "Thor",
        "job": "Dios del Trueno"
    }
    
    logger.info(f'{test} - Enviando solicitud PUT a la URL: {url_base}')
    response = requests.post(url_base, headers=header_request, json=payload)

    # VERIFICAR QUE SE HAYA CREADO EL RECURSO
    assert response.status_code == 201, "El recurso no se creo correctamente"
    logger.info(f'{test} - Respuesta recibida con status code: {response.status_code}')
    #print(f'Status code: {response.status_code}')

    data = response.json()

    # Mostrar el JSON formateado
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # VERIFICAR QUE EL NOMBRE EN LA RESPUESTA SEL EL MISMO QUE SE HAYA ENVIADO
    assert data["name"] == payload["name"], "El nombre no coincide"
    logger.info(f"{test} - El nombre enviado {payload["name"]} coincide con el recibido: {data["name"]}")
    #print(f'El nombre enviado coincide con el recibido: {data["name"]}')

    # VERIFICAR QUE EN LA RESPUESTA EXIATA UN ID
    assert "id" in data, "No se encontro el ID en la respuesta"
    logger.info(f'{test} - ID del usuario creado: {data["id"]}')
    #print(f'ID del usuario creado: {data["id"]}')

    # VERIFICAR QUE EN LA RESPUESTA EXISTA UNA FECHA DE CREACION
    assert "createdAt" in data, "No se encontro la fecha de creacion en la respuesta"
    logger.info(f'{test} - Fecha de creacion del usuario: {data["createdAt"]}')
    #print(f'Fecha de creacion del usuario: {data["createdAt"]}')