# DATA FROM:
# https://github.com/dr5hn/countries-states-cities-database/tree/master
# Thanks!

import json

def extract_data(data):
    extracted_data = []

    for country in data:
        country_data = {
            "name": country['name'],
            "iso3": country.get('iso3', ''),
            "iso2": country.get('iso2', ''),
            "phone_code": country.get('phone_code', ''),
            "capital": country.get('capital', ''),
            "currency": country.get('currency', ''),
            "currency_symbol": country.get('currency_symbol', ''),
            "native": country.get('native', ''),
            "region": country.get('region', ''),
            "nationalities": [country.get('nationality', '')],
            "states": []
        }

        for state in country.get('states', []):
            state_data = {
                "name": state['name'],
                "cities": [city['name'] for city in state.get('cities', [])[:50]]
                # Limit to 50, because we don't need all, right?
            }
            country_data["states"].append(state_data)

        existing_country = next((c for c in extracted_data if c['name'] == country_data['name']), None)
        if existing_country:
            existing_country['nationalities'].append(country_data['nationalities'][0])
        else:
            extracted_data.append(country_data)

    return extracted_data

def export_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

def read():
    path = "countries+states+cities.json"

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    extracted_data = extract_data(data)
    export_to_json(extracted_data, "translations_and_data.json")
