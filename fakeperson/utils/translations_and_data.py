import json

data = []

def read():
    global data
    path = "data/translations_and_data.json"
    # STATES HAVE MAX 50 CITY TO SAVE SPACE

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

def get_measurement_unit(country: str):
    for item in data:
        if item['name'].lower() == country.lower():
            return item['measurement_units']
    raise ValueError(f'Country data for "{country}" not found')

def get_gender_translation(country: str):
    for item in data:
        if item['name'].lower() == country.lower() or item['native'].lower() == country.lower():
            return item['genders_translation']
    raise ValueError(f'Country data for "{country}" not found')