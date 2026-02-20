import requests

def get_page(URL) -> str:
    my_request = requests.get(URL)
    my_request.raise_for_status()
    return my_request.text