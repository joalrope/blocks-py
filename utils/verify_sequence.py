from cgi import print_form
import os
import requests

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={TOKEN}'


def verify_sequence(secuence: str) -> bool:

    print('verificando --------------------')

    get_answer = requests.post(
        api_url,  data={"encoded": secuence})

    json = get_answer.json()

    print('-------------->', json)

    return json['message']
