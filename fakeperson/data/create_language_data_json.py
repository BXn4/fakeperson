import requests
import time
import json
from deep_translator import GoogleTranslator


def extract_data(data):
    extracted_data = []
    for country in data:
        url = f"https://restcountries.com/v3.1/translation/{country['name']}"
        headers = {"Content-Type": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            json_response = response.json()
            try:
                languages_raw = json_response[0]['languages']
                languages = list(languages_raw.values())
                language = languages[0]
            except KeyError:
                language = "Unknown"
        else:
            language = "Unknown"

        time.sleep(0.2)
        height = "CM"
        weight = "KG"
        if country.get('region') == "Americas":
            height = "FEET"
            weight = "LB"


        male = "Male"
        female = "Female"
        chinese = "Chinese"
        spanish = "Spanish"
        english = "English"
        portuguese = "Portuguese"
        russian = "Russian"
        french = "French"
        polish = "Polish"
        german = "German"

        language = language.lower()
        supported = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
        if language != "unknown" and language in supported:
            male = GoogleTranslator(source='en', target=language).translate(male)
            female = GoogleTranslator(source='en', target=language).translate(female)
            chinese = GoogleTranslator(source='en', target=language).translate(chinese)
            spanish = GoogleTranslator(source='en', target=language).translate(spanish)
            english = GoogleTranslator(source='en', target=language).translate(english)
            portuguese = GoogleTranslator(source='en', target=language).translate(portuguese)
            russian = GoogleTranslator(source='en', target=language).translate(russian)
            french = GoogleTranslator(source='en', target=language).translate(french)
            polish = GoogleTranslator(source='en', target=language).translate(polish)
            german = GoogleTranslator(source='en', target=language).translate(german)

        maleFemale = {"Male": male.capitalize(), "Female": female.capitalize()}

        translation_targets = {"Chinese": chinese.capitalize(), "English": english.capitalize(), "French": french.capitalize(), "German": german.capitalize(),
                               "Polish": polish.capitalize(), "Portuguese": portuguese.capitalize(), "Russian": russian.capitalize(),
                               "Spanish": spanish.capitalize()}


        country_data = {
            "name": country['name'],
            "region": country.get('region', ''),
            "iso3": country.get('iso3', ''),
            "iso2": country.get('iso2', ''),
            "native": country.get('native', ''),
            "nationalities": [country.get('nationalities', '')],
            "language": (language.capitalize()),
            "languages_translation": translation_targets,
            "genders_translation": maleFemale,
            "measurement_units": {
                "height": height,
                "weight": weight
            },
        }

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
    path = "data/countries_states_cities.json"

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    extracted_data = extract_data(data)
    export_to_json(extracted_data, "translations_and_data.json")
