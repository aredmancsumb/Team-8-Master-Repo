import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']

def defineApi(user_search):
    data = []
    results = []

    params = {
        'search': user_search
    }

    for url in swapi_urls:
        r = requests.get(url, params=params)
        data.append(r.json())
    pprint(data)
    for api in data:
        if api['count'] >= 1:
            if api == data[0]:
                results.append(searchFilms(data[0]))
            elif api == data[1]:
                results.append(searchPerson(data[1]))
            elif api == data[2]:
                results.append(searchPlanet(data[2]))
            elif api == data[3]:
                results.append(searchSpecies(data[3]))
            elif api == data[4]:
                results.append(searchStarShips(data[4]))
            elif api == data[5]:
                results.append(searchVehicles(data[5]))
    if user_search == '':
        results = ''
    elif user_search in 'planets':
        r = requests.get(swapi_urls[2], params={'search':''})
        data.append(r.json())
        results.append(searchPlanet(data[6]))
    elif user_search in 'films':
        r = requests.get(swapi_urls[0], params={'search':''})
        data.append(r.json())
        results.append(searchFilms(data[6]))
    elif user_search in 'starships':
        r = requests.get(swapi_urls[4], params={'search':''})
        data.append(r.json())
        results.append(searchPerson(data[6]))
    elif user_search in 'species':
        r = requests.get(swapi_urls[3], params={'search':''})
        data.append(r.json())
        results.append(searchPerson(data[6]))
    elif user_search in 'vehicles':
        r = requests.get(swapi_urls[5], params={'search':''})
        data.append(r.json())
        results.append(searchVehicles(data[6]))
    else:
        filter(user_search, ['people', 'persons', 'characters'])
        r = requests.get(swapi_urls[1], params={'search':''})
        data.append(r.json())
        results.append(searchPerson(data[6]))
    return results


def searchPerson(user_search):
    final = None
    name_ = None
    height = None
    mass = None
    gender = None
    birth_year = None
    skin_color = None
    eye_color = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Height: ', 'Mass: ', 'Gender: ', 'Birth year: ', 'Skin color: ', 'Eye color: ']

    for results in user_search['results']:
        info = ['People']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['height'])
        info.append(user_search['results'][index]['mass'])
        info.append(user_search['results'][index]['gender'])
        info.append(user_search['results'][index]['birth_year'])
        info.append(user_search['results'][index]['skin_color'])
        info.append(user_search['results'][index]['eye_color'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchPlanet(user_search):
    final = None
    name_ = None
    rotation_period = None
    orbital_period = None
    diameter = None
    gravity = None
    population = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Diameter: ', 'Gravity: ', 'Population: ', 'Rotation period: ', 'Orbital period: ']

    for results in user_search['results']:
        info = ['Planets']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['rotation_period'])
        info.append(user_search['results'][index]['orbital_period'])
        info.append(user_search['results'][index]['diameter'])
        info.append(user_search['results'][index]['gravity'])
        info.append(user_search['results'][index]['population'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchStarShips(user_search):
    final = None
    name_ = None
    model = None
    cost_in_credits = None
    length = None
    crew = None
    cargo_capacity = None
    consumables = None
    hyperdrive_rating = None
    starship_class = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Model: ', 'Cost in credits: ', 'Length: ', 'Crew: ', 'Cargo capacity: ', 'Consumables: ', 'Hyperdrive rating: ', 'Starship class: ']

    for results in user_search['results']:
        info = ['Starships']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['model'])
        info.append(user_search['results'][index]['cost_in_credits'])
        info.append(user_search['results'][index]['length'])
        info.append(user_search['results'][index]['crew'])
        info.append(user_search['results'][index]['cargo_capacity'])
        info.append(user_search['results'][index]['consumables'])
        info.append(user_search['results'][index]['hyperdrive_rating'])
        info.append(user_search['results'][index]['starship_class'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchSpecies(user_search):
    final = None
    name_ = None
    classification = None
    designation = None
    average_height = None
    average_lifespan = None
    language = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Classification: ', 'Designation: ', 'Average height: ', 'Average lifespan: ', 'Language: ']

    for results in user_search['results']:
        info = ['Species']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['classification'])
        info.append(user_search['results'][index]['designation'])
        info.append(user_search['results'][index]['average_height'])
        info.append(user_search['results'][index]['average_lifespan'])
        info.append(user_search['results'][index]['language'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchVehicles(user_search):
    final = None
    name_ = None
    model = None
    manufacturer = None
    cost_in_credits = None
    passengers = None
    cargo_capacity = None
    vehicle_class = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Model: ', 'Manufacturer: ', 'Cost in credits: ', 'Passengers: ', 'Cargo capacity: ', 'Vehicle class: ']

    for results in user_search['results']:
        info = ['Vehicles']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['model'])
        info.append(user_search['results'][index]['manufacturer'])
        info.append(user_search['results'][index]['cost_in_credits'])
        info.append(user_search['results'][index]['passengers'])
        info.append(user_search['results'][index]['cargo_capacity'])
        info.append(user_search['results'][index]['vehicle_class'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchFilms(user_search):
    final = None
    title = None
    episode_id = None
    director = None
    producer = None
    release_date = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Title: ', 'Episode ID: ', 'Director: ', 'Producer: ', 'Release date: ']

    for results in user_search['results']:
        info = ['Films']
        info.append(user_search['results'][index]['title'])
        info.append(user_search['results'][index]['episode_id'])
        info.append(user_search['results'][index]['director'])
        info.append(user_search['results'][index]['producer'])
        info.append(user_search['results'][index]['release_date'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result
