import requests
import os
from dotenv import load_dotenv
from typing import Dict, List
from ..mocks.blocks import blocks_mock


load_dotenv()

TOKEN = os.getenv('TOKEN')


def are_consecutive(block1: str, block2: str, token: str) -> bool:

    api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={token}'

    test_blocks: Dict[str, List[str]] = {"blocks": [
        block1,
        block2
    ]}

    is_sorted_req = requests.post(api_url, json=test_blocks)

    is_sorted_json = is_sorted_req.json()

    is_sorted = is_sorted_json['message']

    return is_sorted


print(are_consecutive(blocks_mock[1], blocks_mock[5], TOKEN))
