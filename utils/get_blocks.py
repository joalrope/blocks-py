import os
import requests
from dotenv import load_dotenv
from typing import List

load_dotenv()

TOKEN = os.getenv('TOKEN')

api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={TOKEN}'

print(api_url)


def get_blocks() -> List[str]:
    blocks_req = requests.get(api_url)

    print('rquest =====>: ', blocks_req)

    blocks_json = blocks_req.json()

    print(blocks_json['data'])

    return blocks_json['data']


print(get_blocks())
