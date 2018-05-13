import requests
from pprint import pprint


swapi_urls = ['https://swapi.co/api/films/', 'https://swapi.co/api/people/', 'https://swapi.co/api/planets/', 'https://swapi.co/api/species/', 'https://swapi.co/api/starships/', 'https://swapi.co/api/vehicles/']

def defineApi(user_search):
    data = []
    results = []
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
                results.append(searchFilms(data[0]))
            if api == data[1]:
                results.append(searchPerson(data[1]))
            if api == data[2]:
                results.append(searchPlanet(data[2]))
            if api == data[3]:
                results.append(searchSpecies(data[3]))
            if api == data[4]:
                results.append(searchStarShips(data[4]))
            if api == data[5]:
                results.append(searchVehicles(data[5]))
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
    info = []
    index = 0
    titles = ['Category', 'Name: ', 'Height: ', 'Mass: ', 'Gender: ', 'Birth year: ', 'Skin color: ', 'Eye color: ']
    print('people: ' + str(len(user_search['results'])))
    for results in user_search['results']:
        category = 'People'
        name_ = user_search['results'][index]['name']
        height = user_search['results'][index]['height']
        mass = user_search['results'][index]['mass']
        gender = user_search['results'][index]['gender']
        birth_year = user_search['results'][index]['birth_year']
        skin_color = user_search['results'][index]['skin_color']
        eye_color = user_search['results'][index]['eye_color']
        index += 1
        info.extend([category, name_, height, mass, gender, birth_year, skin_color, eye_color])
    if len(results) > 1:
        index += 1
        zipped = list(zip(titles * index, info))
    else:
        zipped = list(zip(titles, info))
    return zipped

def searchPlanet(user_search):
    final = None
    name_ = None
    rotation_period = None
    orbital_period = None
    diameter = None
    gravity = None
    population = None
    info = []
    index = 0
    titles = ['Category', 'Name: ', 'Diameter: ', 'Gravity: ', 'Population: ', 'Rotation period: ', 'Orbital period: ']
    print('planet: ' + str(len(user_search['results'])))
    for results in user_search['results']:
        category = 'Planets'
        name_ = user_search['results'][index]['name']
        rotation_period = user_search['results'][index]['rotation_period']
        orbital_period = user_search['results'][index]['orbital_period']
        diameter = user_search['results'][index]['diameter']
        gravity = user_search['results'][index]['gravity']
        population = user_search['results'][index]['population']
        index += 1
        info.extend([category, name_, rotation_period, orbital_period, diameter, gravity, population])
    if len(results) > 1:
        index += 1
        zipped = list(zip(titles * index, info))
    else:
        zipped = list(zip(titles, info))
    return zipped

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
    info = []
    index = 0
    titles = ['Category', 'Name: ', 'Model: ', 'Cost in credits: ', 'Length: ', 'Crew: ', 'Cargo capacity: ', 'Consumables: ', 'Hyperdrive rating: ', 'Starship class: ']

    for results in user_search['results']:
        category = 'Starships'
        name_ = user_search['results'][index]['name']
        model= user_search['results'][index]['model']
        cost_in_credits= user_search['results'][index]['cost_in_credits']
        length = user_search['results'][index]['length']
        crew = user_search['results'][index]['crew']
        cargo_capacity = user_search['results'][index]['cargo_capacity']
        consumables = user_search['results'][index]['consumables']
        hyperdrive_rating = user_search['results'][index]['hyperdrive_rating']
        starship_class= user_search['results'][index]['starship_class']
        index += 1
        info.extend([category, name_, model, cost_in_credits, length, crew, cargo_capacity, consumables, hyperdrive_rating, starship_class])
    if len(results) > 1:
        index += 1
        zipped = list(zip(titles * index, info))
    else:
        zipped = list(zip(titles, info))
    return zipped

def searchSpecies(user_search):
    final = None
    name_ = None
    classification = None
    designation = None
    average_height = None
    average_lifespan = None
    language = None
    info = []
    index = 0
    titles = ['Category', 'Name: ', 'Classification: ', 'Designation: ', 'Average height: ', 'Average lifespan: ', 'Language: ']

    for results in user_search['results']:
        category = 'Species'
        name_ = user_search['results'][index]['name']
        classification = user_search['results'][index]['classification']
        designation = user_search['results'][index]['designation']
        average_height = user_search['results'][index]['average_height']
        average_lifespan = user_search['results'][index]['average_lifespan']
        language = user_search['results'][index]['language']
        index += 1
        info.extend([category, name_, classification, designation, average_height, average_lifespan, language])
    if len(results) > 1:
        index += 1
        zipped = list(zip(titles * index, info))
    else:
        zipped = list(zip(titles, info))
    return zipped

def searchVehicles(user_search):
    final = None
    name_ = None
    model = None
    manufacturer = None
    cost_in_credits = None
    passengers = None
    cargo_capacity = None
    vehicle_class = None
    info = []
    index = 0
    titles = ['Category', 'Name: ', 'Model: ', 'Manufacturer: ', 'Cost in credits: ', 'Passengers: ', 'Cargo capacity: ', 'Vehicle class: ']
    print('vehicles: ' + str(len(user_search['results'])))
    for results in user_search['results']:
        category = 'Vehicles'
        name_ = user_search['results'][index]['name']
        model = user_search['results'][index]['model']
        manufacturer = user_search['results'][index]['manufacturer']
        cost_in_credits = user_search['results'][index]['cost_in_credits']
        passengers = user_search['results'][index]['passengers']
        cargo_capacity = user_search['results'][index]['cargo_capacity']
        vehicle_class = user_search['results'][index]['vehicle_class']
        index += 1
        info.extend([category, name_, model, manufacturer, cost_in_credits, passengers, cargo_capacity, vehicle_class])
    if len(results) > 1:
        index += 1
        zipped = list(zip(titles * index, info))
    else:
        zipped = list(zip(titles, info))
    return zipped

def searchFilms(user_search):
    final = None
    title = None
    episode_id = None
    director = None
    producer = None
    release_date = None
    info = []
    index = 0
    titles = ['Category', 'Title: ', 'Episode ID: ', 'Director: ', 'Producer: ', 'Release date: ']
    print('films: ' + str(len(user_search['results'])))
    for results in user_search['results']:
        category = 'Films'
        title = user_search['results'][index]['title']
        episode_id = user_search['results'][index]['episode_id']
        director = user_search['results'][index]['director']
        producer = user_search['results'][index]['producer']
        release_date = user_search['results'][index]['release_date']
        index += 1
        info.extend([category, title, episode_id, director, producer, release_date])
    if len(results) > 1:
        index += 1
        zipped = list(zip(titles * index, info))
    else:
        zipped = list(zip(titles, info))
    return zipped
