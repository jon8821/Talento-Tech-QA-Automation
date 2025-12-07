import requests
import pytest
import json
from utils.logger import logger

@pytest.mark.api
@pytest.mark.reqres
def test_api_get_users(url_base,header_request):
    test = "Test API GET"
    url = f"{url_base}/2"

    logger.info(f"Iniciando '{test}'")

    logger.info(f"{test} - Realizando solicitud GET a la URL: {url}")
    response = requests.get(url,headers=header_request)

    # VERIFICAR QUE LA RESPUESTA SEA EXITOSA
    assert response.status_code == 200
    logger.info(f'{test} - Respuesta recibida con status code: {response.status_code}')
    #print(f'Status code: {response.status_code}')

    data = response.json()

    # Mostrar el JSON formateado
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
    # VERIFICAR QUE LA CLAVE "DATA" ESTA PRESENTE
    assert "data" in data
    logger.info(f'{test} - La clave "data" está presente en la respuesta.')
    #print(f'La clave "data" está presente en la respuesta.')

    # VERIFICAR QUE HAYA AL MENOS UN USUARIO EN LA LISTA
    assert len(data["data"]) > 0
    logger.info(f'{test} - Existe al menos 1 usuario en la lista.')
    #print('Existe al menos 1 usuario en la lista.')