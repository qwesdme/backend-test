import requests


def data_dict(url: str) -> dict:
    r = requests.get(url)
    json_data = r.json()
    return json_data
