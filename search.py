import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']
search_list = ['name', 'height', 'gender', 'birth_year']
def searchApi(user_search, search_list):
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
                name_ = api['results'][0][search_list]

                #api['results'][0]
                #pprint(api)



    return name_
                #api in dictionary -> get info
def searchHeight(user_search):
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

                height = api['results'][0]['height']

                #api['results'][0]
                #pprint(api)



    return height
def searchGender(user_search):
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

                gender = api['results'][0]['gender']

                #api['results'][0]
                #pprint(api)



    return gender
def searchYear(user_search):
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

                birth_year = api['results'][0]['birth_year']

                #api['results'][0]
                #pprint(api)



    return birth_year
