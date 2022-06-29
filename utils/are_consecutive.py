import requests
import os

from dotenv import load_dotenv
from typing import Dict, List


load_dotenv()

TOKEN = os.getenv('TOKEN')


def are_consecutive(block1: str, block2: str, token: str) -> bool:

    api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={token}'

    test_blocks: Dict[str, List[str]] = {"blocks": [
        block1,
        block2
    ]}

    is_sorted_req: requests.Response = requests.post(api_url, json=test_blocks)

    is_sorted_json: Dict[str, bool] = is_sorted_req.json()

    is_sorted: bool = is_sorted_json['message']

    return is_sorted
