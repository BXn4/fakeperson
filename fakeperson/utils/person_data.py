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


def get_height(age: int, gender: str or int, nationality: str, native: bool = False):
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
    match person_gender:
        case "Female":
            if age >= 18:
                height = randint(150, 175)  # CM
            elif age <= 12:
                height = randint(90, 125)  # CM
            else:
                height = randint(120, 160)  # CM
            if nationality == "American":
                height = round((height / 30.48), 2)  # TO FEET
        case "Male":
            if age >= 18:
                height = randint(160, 210)  # CM
            elif age <= 12:
                height = randint(100, 130)  # CM
            else:
                height = randint(150, 175)  # CM
            if nationality == "American":
                height = round((height / 30.48), 2)  # TO FEET

    return height
