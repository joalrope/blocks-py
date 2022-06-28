import os
import requests
from dotenv import load_dotenv
from ...blocks import ordered_sequence_mock

load_dotenv()

TOKEN = os.getenv('TOKEN')

api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={TOKEN}'


def verify_sequence() -> bool:
    get_answer = requests.post(
        api_url,  data={"encoded": ordered_sequence_mock})

    json = get_answer.json()

    print('es correcto?:', json)


print(verify_sequence())
