import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']

def searchPerson(user_search):
    final = None
    for url in swapi_urls:

        params = {
        'search': user_search
        }

        r = requests.get(url, params=params)
        data = []
        data.append(r.json())

        for api in data:
            if api['count'] >= 1:
                #final = api['results'][0]

                    name_ = api['results'][0]['name']
                    height = api['results'][0]['height']
                    mass = api['results'][0]['mass']
                    gender = api['results'][0]['gender']
                    birth_year = api['results'][0]['birth_year']
                    skin_color = api['results'][0]['skin_color']
                    eye_color = api['results'][0]['eye_color']
                #api['results'][0]
                #pprint(api)



    return [name_, height, mass, gender, birth_year, skin_color, eye_color]
                #api in dictionary -> get info
