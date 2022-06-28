import os
import requests
from dotenv import load_dotenv
from typing import List
from utils.are_consecutive import are_consecutive
from mocks.blocks import blocks_mock, ordered_sequence_mock

load_dotenv()

TOKEN = os.getenv('TOKEN')

api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={TOKEN}'

get_answer = requests.post(api_url,  data={"encoded": ordered_sequence_mock})

json = get_answer.json()
print('es correcto?:', json)

# result = json['encoded']


def check(blocks: List[str], token: str) -> List[str]:
    # Desarrollar aquí dentro el algoritmo que ordene los bloques, usando la API "/check".
    # IMPORTANTE: observar que está recibiendo un parámetro "token".
    # El mismo es para usarlo en la llamada a la API.

    array_ordenado = are_consecutive(blocks[1], blocks[5], token)

    print(array_ordenado)

    return array_ordenado


print(check(blocks_mock, TOKEN))
