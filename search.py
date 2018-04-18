import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']

user_search = input('Search:')


for url in swapi_urls:

    payload = {
    'search': user_search
    }

    r = requests.get(url, params=payload)
    data = r.json()
    pprint(data)
