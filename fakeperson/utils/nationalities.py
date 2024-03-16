# DATA FROM:
# https://github.com/dr5hn/countries-states-cities-database/tree/master
# Thanks!

# Code looks a little-bit terrible, but it's working as excepted.

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
    # IN: NAT*
    # IN: NATIVE
    # OUT: NAT FROM THE DATA

    # Check the nationality if valid
    # If native, return in native
    # There's can be multiple in native
    for item in data:
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
    # IN: COUNTRY*
    # IN: NATIVE
    # OUT: COUNTRY FROM DATA

    # Check if the country is valid
    # If native, return in native
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
    # IN: CITY*
    # OUT: CITY FROM DATA

    # Check if the city is valid
    # No native support.
    for item in data:
        for state in item.get('states', []):
            for cities in state.get('cities', []):
                if city.lower() in cities.lower():
                    return cities

    raise ValueError(f'"{city}" is not found')


def get_fake_nationality(country: str = None, city: str = None, native: bool = False):
    # IN: COUNTRY
    # IN: CITY:
    # IN: NATIVE
    # OUT: NAT FROM THE DATA

    # Get nationality from country, or from city. If native, return in native.
    # If not country, or city, return random nationality
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
    # IN: NAT
    # IN: CITY
    # IN: NATIVE
    # OUT: COUNTRY FROM THE DATA

    # Get country from nationality, or from city. If native, return in native.
    # If not nationality, or city, return a random country.
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


def get_fake_state(nationality: str = None, country: str = None, city: str = None):
    # IN: NAT
    # IN: COUNTRY
    # IN: CITY
    # OUT: STATE FROM DATA

    # Get random state from nationality, or from country, or from city.
    # If not nationality, or country, or city, return random state

    states = []
    if nationality:
        for item in data:
            nationalities = item.get('nationalities', [])
            all_nats = ','.join(map(str, nationalities))  # Convert list to str
            nats = all_nats.split(', ')
            nat = nats[0].strip()
            if len(nationality) == 3:
                if item['iso3'].lower() == nationality.lower():
                    nationality = nat

            match len(nats):
                case 2:
                    nat2 = nats[1].strip()
                    if nat2.lower() == nationality.lower():
                        nationality = nats[0].strip()
                case 3:
                    nat3 = nats[2].strip()
                    if nat3.lower() == nationality.lower():
                        nationality = nats[0].strip()
                case 4:
                    nat3 = nats[3].strip()
                    if nat3.lower() == nationality.lower():
                        nationality = nats[0].strip()

            if nat.lower() == nationality.lower():
                for state in item['states']:
                    if state['cities']:
                        states.append(state['name'])

    if country:
        for item in data:
            if item['name'].lower() == country.lower() or item['native'].lower() == country.lower():
                for state in item['states']:
                    if state['cities']:
                        states.append(state['name'])

    if city:
        for item in data:
            for state in item['states']:
                if state['cities']:
                    cities: list = state['cities']
                    if city.capitalize() in cities:
                        return state['name']

    if not nationality and not country and not city:
        for item in data:
            for state in item['states']:
                if state['cities']:
                    states.append(state['name'])

    if states:
        return choice(states)

    if nationality:
        raise ValueError(f'Theres no states found for the "{nationality}" nationality')

    if country:
        raise ValueError(f'"{country}" does not have any states, or the country not found')

    if city:
        raise ValueError(f'"{city}" does not have any states, or the city not found')

def get_fake_city(nationality: str = None, country: str = None, state: str = None):
    # IN: NAT
    # IN: COUNTRY
    # IN: STATE
    # OUT: RANDOM CITY FROM DATA

    # Get random city from nationality, or from country, or from state.
    # If not nationality, or country, or state, return random city

    cities = []
    if nationality:
        for item in data:
            nationalities = item.get('nationalities', [])
            all_nats = ','.join(map(str, nationalities))  # Convert list to str
            nats = all_nats.split(', ')
            nat = nats[0].strip()
            if len(nationality) == 3:
                if item['iso3'].lower() == nationality.lower():
                    nationality = nat

            match len(nats):
                case 2:
                    nat2 = nats[1].strip()
                    if nat2.lower() == nationality.lower():
                        nationality = nats[0].strip()
                case 3:
                    nat3 = nats[2].strip()
                    if nat3.lower() == nationality.lower():
                        nationality = nats[0].strip()
                case 4:
                    nat3 = nats[3].strip()
                    if nat3.lower() == nationality.lower():
                        nationality = nats[0].strip()

            if nat.lower() == nationality.lower():
                if not item['states']:
                    raise ValueError(f'It looks like "{nationality}" does not have any valid states. Please use different nationality')
                for states in item['states']:
                    if states['cities']:
                        for city in states['cities']:
                            cities.append(city)

    if country:
        for item in data:
            if item['name'].lower() == country.lower() or item['native'].lower() == country.lower():
                for states in item['states']:
                    if states['cities']:
                        for city in states['cities']:
                            cities.append(city)

    if state:
        for item in data:
            for states in item['states']:
                if states['name'].lower() == state.lower():
                    for city in states['cities']:
                        if city:
                            cities.append(city)

    if not nationality and not country and not state:
        for item in data:
            for states in item['states']:
                if states['cities']:
                    for city in states['cities']:
                        cities.append(city)

    if cities:
        return choice(cities)

    if nationality:
        raise ValueError(f'Theres no cities found for the "{nationality}" nationality')

    if country:
        raise ValueError(f'"{country}" does not have any cities, or the country not found')

    if state:
        raise ValueError(f'"{state}" does not have any cities, or the state not found')
