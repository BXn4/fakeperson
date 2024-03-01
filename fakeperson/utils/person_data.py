from random import choice, randint
from utils import translations_and_data


def age():
    return randint(5, 100)

def get_gender(gender: str or int = None, country: str = None, native: bool = False):
    if not gender:  # set random gender if gender is none
        gender = randint(1, 2)

    if isinstance(gender, int):  # Check gender
        match gender:
            case 1:  # Male
                person_gender = "Male"
            case 2:  # Female
                person_gender = "Female"
            case _:  # Default
                person_gender = choice(["Male", "Female"])
    elif isinstance(gender, str):
        if gender.lower() in ["male", "female"]:
            person_gender = gender.capitalize()
        else:  # When the input is not male or female
            person_gender = choice(["Male", "Female"])

    if not native:
        return person_gender
    elif native:
        if not country:
            raise ValueError('Please enter a valid country name to use the native feature')
        translations = translations_and_data.get_gender_translation(country)
        for translated_gender in translations:
            if translated_gender == person_gender:
                return translations[translated_gender]


def get_height(age: int, gender: str or int, native: bool = False):
    person_gender = gender(gender)
    random_height = randint(100, 140)

