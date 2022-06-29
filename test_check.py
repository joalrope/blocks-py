import os

from dotenv import load_dotenv
from typing import List

from main import *
from utils.blocks import blocks_mock
from utils.verify_sequence import verify_sequence

load_dotenv()

TOKEN = os.getenv('TOKEN')

blocks: List[str] = blocks_mock


def test_check():
    assert verify_sequence(check(blocks, TOKEN)) == True
