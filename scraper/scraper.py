import requests

def get_page(URL):
    my_request = requests.get(URL)
    my_request.raise_for_status()
    print(my_request.text)