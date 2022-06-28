# import requests
# from typing import List
# from main import check

# blocks: List[str] = ['hy5tre3was4e', 'lmhgdjfdsysa', 'ikjfsxbvolkz']

# token: str = '9569a527-464f-4ccd-9c1a-ed794dc7a0b3'


# def test_test():
#     api_url: str = f'https://rooftop-career-switch.herokuapp.com/check?token={token}'

#     is_sorted = requests.get(api_url)

#     json = is_sorted.json()

#     result = json['encoded']

#     check(blocks, token)

#     assert check(blocks, token) == [result]
