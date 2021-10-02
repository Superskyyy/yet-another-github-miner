import requests

"""
Not working, api not enough
"""


def filter_qualified():
    res = requests.get(f'https://api.github.com/search/code?q=filename:MLProject')
    return res.text


if __name__ == "__main__":
    print(filter_qualified())
