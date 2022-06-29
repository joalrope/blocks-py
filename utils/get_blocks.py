import os
import requests

from dotenv import load_dotenv
from typing import List

load_dotenv()

TOKEN = os.getenv('TOKEN')

api_url: str = f'https://rooftop-career-switch.herokuapp.com/blocks?token={TOKEN}'


def get_blocks() -> List[str]:
    blocks_req = requests.get(api_url)

    blocks_json = blocks_req.json()

    return blocks_json['data']
