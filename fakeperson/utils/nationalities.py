# DATA FROM:
# https://github.com/dr5hn/countries-states-cities-database/tree/master
# Thanks!

import json
from random import choice, randint

data = []


# TODO: to make it faster, switch to match-case


def read():
    global data
    path = "data/countries_states_cities.json"
    # STATES HAVE MAX 50 CITY TO SAVE SPACE

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)


def check_nationality(nationality: str, native: bool):
    for item in data:
        all_nats = ','.join(map(str, item['nationalities']))  # Convert list to str
        all_nats = ','.join(map(str, item['nationalities']))  # Convert list to str
        nats = all_nats.split(',')
        nat1 = nats[0].strip()
        nat2 = None
        if len(nationality) == 3:
            if item['iso3'].lower() == nationality.lower():
                nationality = nat1
                if native:
                    if len(nats) == 2:
                        nat2 = nats[1].strip()
                        nationality = nat2
        match len(nats):
            case 2:
                nat2 = nats[1].strip()
                if nat2.lower() == nationality.lower():
                    if native:
                        return nat2
                    return nat1
            case 3:
                nat3 = nats[2].strip()
                if nat3.lower() == nationality.lower():
                    if native:
                        return nat3
                    return nat1
            case 4:
                nat4 = nats[3].strip()
                if nat4.lower() == nationality.lower():
                    if native:
                        return nat4
                    return nat1
            # Use the native language
        if nat1.lower() == nationality.lower():
            if nat2:
                if native:
                    return nat2
            return nat1

    raise ValueError(f'"{nationality}" is not found')


def check_country(country: str, native: bool):
    for item in data:
        if item['name'].lower() == country.lower():
            if native:
                return item['native']
            return item['name']

        elif item['native'] is not None and item['native'].lower() == country.lower():
            if native:
                return item['native']
            return item['name']

    raise ValueError(f'"{country}" is not found')


def check_city(city: str):
    for item in data:
        for state in item.get('states', []):
            for cities in state.get('cities', []):
                if city.lower() in cities.lower():
                    return cities

    raise ValueError(f'"{city}" is not found')


def get_fake_nationality(country: str = None, city: str = None, native: bool = False):
    if country:
        for item in data:
            if item['name'].lower() == country.lower():
                nationality = ','.join(map(str, item['nationalities']))  # Convert list to str
                nats = nationality.split(', ')
                if native:
                    if len(nats) == 2:
                        return nats[1]
                        # Use the native language
                return nats[0]

            elif item['native'] is not None and item['native'].lower() == country.lower():
                nationality = ','.join(map(str, item['nationalities']))  # Convert list to str
                nats = nationality.split(', ')
                if native:
                    if len(nats) == 2:
                        return nats[1]
                        # Use in the native language
                return nats[0]
    if country:
        raise ValueError(f'"{country}" is not found')

    elif city:
        for item in data:
            for state in item.get('states', []):
                for cities in state.get('cities', []):
                    if cities.lower() == city.lower():
                        nationality = ','.join(map(str, item['nationalities']))  # Convert list to str
                        nats = nationality.split(', ')
                        if native:
                            if len(nats) == 2:
                                return nats[1].strip()
                                # Use the nationality in the country native language
                        return nats[0].strip()

    if city:
        raise ValueError(f'"{city}" is not found')

    # If not country or city given, return random
    rnd = randint(0, len(data) - 1)
    nationality = ','.join(map(str, data[rnd]['nationalities']))  # Convert list to str
    nats = nationality.split(',')
    if native:
        if len(nats) == 2:
            return nats[1].strip()
        # Use the nationality in the country native language
    return nats[0].strip()


def get_fake_country(nationality: str = None, city: str = None, native: bool = False):
    if nationality:
        for item in data:
            nationalities = item.get('nationalities', [])
            all_nats = ','.join(map(str, nationalities))  # Convert list to str
            nats = all_nats.split(', ')
            nat1 = nats[0].strip()
            if len(nationality) == 3:
                if item['iso3'].lower() == nationality.lower():
                    nationality = nat1
            match len(nats):
                case 2:
                    nat2 = nats[1].strip()
                    if nat2.lower() == nationality.lower():
                        if native:
                            return item['native']
                        return item['name']
                case 3:
                    nat3 = nats[2].strip()
                    if nat3.lower() == nationality.lower():
                        if native:
                            return item['native']
                        return item['name']
                case 4:
                    nat4 = nats[3].strip()
                    if nat4.lower() == nationality.lower():
                        if native:
                            return item['native']
                        return item['name']
            if nat1.lower() == nationality.lower():
                if native:
                    return item['native']
                return item['name']

    if city:
        for item in data:
            for state in item.get('states', []):
                for cities in state.get('cities', []):
                    if cities.lower() == city.lower():
                        if native:
                            return item['native']
                        return item['name']

    if nationality or city:
        raise ValueError(f'Nationality: "{nationality}" or City: "{city}" not found')

    rnd = randint(0, len(data) - 1)
    return data[rnd]['name']  # Return random country


def get_fake_city(nationality: str = None, country: str = None, native: bool = False):
    pass

