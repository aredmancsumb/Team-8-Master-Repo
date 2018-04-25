import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']

def searchApi(user_search):
    count = 0
    for url in swapi_urls:

        params = {
        'search': user_search
        }

        r = requests.get(url, params=params)
        data = []
        data.append(r.json())
        \
        for api in data:
            if api['count'] >= 1:
                pprint(api)
                count += 1
                
    if count == 0:
        pprint("try Again")

                #api in dictionary -> get info
