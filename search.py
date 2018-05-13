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
    if user_search == '':
        results = []
    return results



def searchPerson(user_search):
    final = None
    name_ = None
    height = None
    mass = None
    gender = None
    hair_color = None
    birth_year = None
    skin_color = None
    eye_color = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Height: ', 'Mass: ', 'Gender: ', 'Hair Color: ', 'Birth year: ', 'Skin color: ', 'Eye color: ']

    for results in user_search['results']:
        info = ['People']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['height'] + " cm")
        info.append(user_search['results'][index]['mass'] + " kg")
        info.append(user_search['results'][index]['gender'])
        info.append(user_search['results'][index]['hair_color'])
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
    climate = None
    terrain = None
    surface_water = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Diameter: ', 'Gravity: ', 'Population: ', 'Rotation period: ', 'Orbital period: ', 'Climate: ', 'Terrain: ', 'Surface Water: ']

    for results in user_search['results']:
        info = ['Planets']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['diameter'] + ' km')
        info.append(user_search['results'][index]['gravity'])
        info.append(user_search['results'][index]['population'])
        info.append(user_search['results'][index]['rotation_period'] + ' Hours')
        info.append(user_search['results'][index]['orbital_period'] + ' Days')
        info.append(user_search['results'][index]['climate'])
        info.append(user_search['results'][index]['terrain'])
        info.append(user_search['results'][index]['surface_water'] + '%')
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
    passengers = None
    cargo_capacity = None
    consumables = None
    hyperdrive_rating = None
    max_atmosphering_speed = None
    MGLT = None
    starship_class = None
    manufacturer = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Model: ', 'Cost in credits: ', 'Length: ', 'Manufacturer', 'Crew: ', 'Passengers:', 'Cargo capacity: ', 'Consumables: ', 'Hyperdrive rating: ', 'Max Atmosphering Speed:', 'Max Megalights per Hour:', 'Starship class: ']

    for results in user_search['results']:
        info = ['Starships']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['model'])
        info.append(user_search['results'][index]['cost_in_credits'])
        info.append(user_search['results'][index]['length'] + ' m')
        info.append(user_search['results'][index]['manufacturer'])
        info.append(user_search['results'][index]['crew'])
        info.append(user_search['results'][index]['passengers'])
        info.append(user_search['results'][index]['cargo_capacity'] + ' kg')
        info.append(user_search['results'][index]['consumables'])
        info.append(user_search['results'][index]['hyperdrive_rating'])
        info.append(user_search['results'][index]['max_atmosphering_speed'])
        info.append(user_search['results'][index]['MGLT'])
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
    eye_colors = None
    hair_colors = None
    skin_colors = None
    language = None
    homeworld = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Classification: ', 'Designation: ', 'Average height: ', 'Average lifespan: ', 'Eye Colors: ', 'Hair Colors: ', 'Skin Colors: ', 'Language: ']

    for results in user_search['results']:
        info = ['Species']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['classification'])
        info.append(user_search['results'][index]['designation'])
        info.append(user_search['results'][index]['average_height'] + ' cm')
        info.append(user_search['results'][index]['average_lifespan'] + 'years')
        info.append(user_search['results'][index]['eye_colors'])
        info.append(user_search['results'][index]['hair_colors'])
        info.append(user_search['results'][index]['skin_colors'])
        info.append(user_search['results'][index]['language'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchVehicles(user_search):
    final = None
    name_ = None
    model = None
    manufacturer = None
    length = None
    cost_in_credits = None
    crew = None
    passengers = None
    max_atmosphering_speed = None
    cargo_capacity = None
    consumables = None
    vehicle_class = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Name: ', 'Model: ', 'Manufacturer: ', 'Length: ', 'Cost in credits: ', 'Crew: ', 'Passengers: ', 'Cargo capacity: ', 'Max Atmosphering Speed: ', 'Consumables: ', 'Vehicle class: ']

    for results in user_search['results']:
        info = ['Vehicles']
        info.append(user_search['results'][index]['name'])
        info.append(user_search['results'][index]['model'])
        info.append(user_search['results'][index]['manufacturer'])
        info.append(user_search['results'][index]['length'] + ' m')
        info.append(user_search['results'][index]['cost_in_credits'])
        info.append(user_search['results'][index]['crew'])
        info.append(user_search['results'][index]['passengers'])
        info.append(user_search['results'][index]['cargo_capacity'] + ' kg')
        info.append(user_search['results'][index]['max_atmosphering_speed'])
        info.append(user_search['results'][index]['consumables'])
        info.append(user_search['results'][index]['vehicle_class'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result

def searchFilms(user_search):
    final = None
    title = None
    episode_id = None
    opening_crawl = None
    director = None
    producer = None
    release_date = None
    final_result = []
    index = 0
    titles = ['Category: ', 'Title: ', 'Episode ID: ', 'Opening Crawl:', 'Director: ', 'Producer: ', 'Release date: ']

    for results in user_search['results']:
        info = ['Films']
        info.append(user_search['results'][index]['title'])
        info.append(user_search['results'][index]['episode_id'])
        info.append(user_search['results'][index]['opening_crawl'])
        info.append(user_search['results'][index]['director'])
        info.append(user_search['results'][index]['producer'])
        info.append(user_search['results'][index]['release_date'])
        index += 1
        final_result.append(list(zip(titles, info)))
    return final_result
