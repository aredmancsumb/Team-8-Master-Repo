import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']

def defineApi(user_search):
    #if search is in what url, then do right function
    data = []
    for url in swapi_urls:

        params = {
        'search': user_search
        }

        r = requests.get(url, params=params)
        data.append(r.json())

    pprint(data)

    for api in data:
        if api['count'] >= 1:
            if api == data[0]:
                return searchFilms(user_search)
            if api == data[1]:
                return searchPerson(user_search)
            if api == data[2]:
                return searchPlanet(user_search)
            if api == data[3]:
                return searchSpecies(user_search)
            if api == data[4]:
                return searchStarShips(user_search)
            if api == data[5]:
                return searchVehicles(user_search)


def searchPerson(user_search):
    final = None
    info = []
    titles = ['Name: ', 'Height: ', 'Mass: ', 'Gender: ', 'Birth year: ', 'Skin color: ', 'Eye color: ']
    for url in swapi_urls:

        params = {
        'search': user_search
        }

        r = requests.get(url, params=params)
        data = []
        data.append(r.json())

        for api in data:
            if api['count'] >= 1:
                index = 0
                for results in api['results']:
                    name_ = api['results'][index]['name']
                    height = api['results'][index]['height']
                    mass = api['results'][index]['mass']
                    gender = api['results'][index]['gender']
                    birth_year = api['results'][index]['birth_year']
                    skin_color = api['results'][index]['skin_color']
                    eye_color = api['results'][index]['eye_color']
                    index += 1

    info.extend([name_, height, mass, gender, birth_year, skin_color, eye_color])
    zipped = list(zip(titles, info))

    return zipped

def searchPlanet(user_search):
    final = None
    info = []
    titles = ['Name: ', 'Diameter: ', 'Gravity: ', 'Population: ', 'Rotation period: ', 'Orbital period: ']
    for url in swapi_urls:

        params = {
            'search': user_search
        }

        r = requests.get(url, params=params)
        data = []
        data.append(r.json())

        for api in data:
            if api['count'] >= 1:
                index = 0
                for results in api['results']:
                    name_ = api['results'][index]['name']
                    rotation_period = api['results'][index]['rotation_period']
                    orbital_period = api['results'][index]['orbital_period']
                    diameter = api['results'][index]['diameter']
                    gravity = api['results'][index]['gravity']
                    population = api['results'][index]['population']
                    index += 1
    info.extend([name_, diameter, gravity, population, rotation_period, orbital_period])
    zipped = list(zip(titles, info))

    return zipped

def searchStarShips(user_search):
    final = None
    info = []
    titles = ['Name: ', 'Model: ', 'Cost in credits: ', 'Length: ', 'Crew: ', 'Cargo capacity: ', 'Consumables: ', 'Hyperdrive rating: ', 'Starship class: ']
    for url in swapi_urls:

        params = {
        'search': user_search
        }

        r = requests.get(url, params=params)
        data = []
        data.append(r.json())

        for api in data:
            if api['count'] >= 1:
                index = 0
                for results in api['results']:
                    name_ = api['results'][index]['name']
                    model= api['results'][index]['model']
                    cost_in_credits= api['results'][index]['cost_in_credits']
                    length = api['results'][index]['length']
                    crew = api['results'][index]['crew']
                    cargo_capacity = api['results'][index]['cargo_capacity']
                    consumables = api['results'][index]['consumables']
                    hyperdrive_rating = api['results'][index]['hyperdrive_rating']
                    starship_class= api['results'][index]['starship_class']
                    index += 1
    info.extend([name_, model, cost_in_credits, length, crew, cargo_capacity, consumables, hyperdrive_rating, starship_class])
    zipped = list(zip(titles, info))
    return zipped

def searchSpecies(user_search):
    final = None
    info = []
    titles = ['Name: ', 'Classification: ', 'Designation: ', 'Average height: ', 'Average lifespan: ', 'Language: ']
    for url in swapi_urls:

        params = {
        'search': user_search
        }

        r = requests.get(url, params=params)
        data = []
        data.append(r.json())

        for api in data:
            if api['count'] >= 1:
                index = []
                for results in api['results']:
                    name_ = api['results'][index]['name']
                    classification = api['results'][index]['classification']
                    designation = api['results'][index]['designation']
                    average_height = api['results'][index]['average_height']
                    average_lifespan = api['results'][index]['average_lifespan']
                    language = api['results'][index]['population']
                    index += 1
    index.extand([name_, classification, designation, average_height, average_lifespan, language])
    zipped = list(zip(titles))
    return zipped

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
