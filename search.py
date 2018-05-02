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
def searchPlanet(user_search):
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
                    rotation_period = api['results'][0]['rotation_period']
                    orbital_period = api['results'][0]['orbital_period']
                    diameter = api['results'][0]['diameter']
                    gravity = api['results'][0]['gravity']
                    population = api['results'][0]['population']

    return [name_, rotation_period, orbital_period, diameter, gravity , population]

def searchStarShips(user_search):
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
                    model= api['results'][0]['model']
                    cost_in_credits= api['results'][0]['cost_in_credits']
                    length = api['results'][0]['length']
                    crew = api['results'][0]['crew']
                    cargo_capacity = api['results'][0]['cargo_capacity']
                    consumables = api['results'][0]['consumables']
                    hyperdrive_rating = api['results'][0]['hyperdrive_rating']
                    starship_class= api['results'][0]['starship_class']

    return [name_, model, cost_in_credits, length, crew, cargo_capacity, consumables, hyperdrive_rating, starship_class]


def searchSpecies(user_search):
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
                    classification = api['results'][0]['classification']
                    designation = api['results'][0]['designation']
                    average_height = api['results'][0]['average_height']
                    average_lifespan = api['results'][0]['average_lifespan']
                    language = api['results'][0]['population']

    return [name_, classification, designation, average_height, average_lifespan, language]

def searchVehicles(user_search):
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
                    model = api['results'][0]['model']
                    manufacturer = api['results'][0]['manufacturer']
                    cost_in_credits = api['results'][0]['cost_in_credits']
                    passengers = api['results'][0]['passengers']
                    cargo_capacity = api['results'][0]['cargo_capacity']
                    vehicle_class = api['results'][0]['vehicle_class']


    return [name_, model, manufacturer, cost_in_credits, passengers, cargo_capacity, vehicle_class]



    def searchFilms(user_search):
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

                        title = api['results'][0]['title']
                        episode_id = api['results'][0]['episode_id']
                        director = api['results'][0]['director']
                        producer = api['results'][0]['producer']
                        release_date = api['results'][0]['release_date']


        return [title, episode_id, director, producer, release_date]
