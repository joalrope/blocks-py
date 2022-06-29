import os
from dotenv import load_dotenv
from typing import List

from utils.are_consecutive import are_consecutive
from utils.get_blocks import get_blocks

load_dotenv()


def check(blocks: List[str], token: str) -> List[str]:
    # Desarrollar aquí dentro el algoritmo que ordene los bloques, usando la API "/check".
    # IMPORTANTE: observar que está recibiendo un parámetro "token".
    # El mismo es para usarlo en la llamada a la API.

    result = [blocks[0]]
    indexes = [0]

    blocks = [b for b in blocks if b != blocks[0]]

    blocks_len = len(blocks)

    while blocks_len > 0:

        previous = result[-1]

        x = 0

        for block in blocks:

            x = x + 1

            if are_consecutive(previous, block, token):
                result.append(block)
                indexes.append(x - 1)
                blocks = [b for b in blocks if b != block]
                break

        blocks_len = len(blocks)

    return ''.join(result)


blocks = get_blocks()
TOKEN = os.getenv('TOKEN')

print(check(blocks, TOKEN))
