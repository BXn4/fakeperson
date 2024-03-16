from math import floor
from typing import Union
from random import randint
from utils import person_data

from utils import nationalities


class Person:
    def __init__(self, gender: Union[int, str], nationality: str, age: int, country: str, city: str,
                 native: bool) -> None:
        self.gender = None  # MALE = 1, FEMALE = 2  # DONE
        self.nationality = None  # DONE
        self.age = None  # DONE
        self.country = None  # DONE
        self.city = None  # DONE

        self.height = None  # DONE
        self.weight = None
        self.eyesColor = None
        self.hairColor = None
        self.wearGlasses = None
        self.glassesDioptre = None

        self.set_random(gender, nationality, age, country, city, native)

        self.address: HomeAddress = HomeAddress()
        self.address.set_random(self)

        self.favFood = None
        self.favDrink = None
        self.favColor = None
        self.favMusicGenre = None

        self.firstname = None
        self.lastname = None
        self.name = None
        self.bornMonth = None
        self.bornDay = None
        self.bornYear = None
        self.birthday = None
        self.isDead = None
        self.mother = None  # Set it in class Parents. ex: person.mother.name
        self.dad = None  # Set it in class Parents. ex: person.dad.name
        self.partner = None  # Set in class Family ex: person.partner.name
        self.isMarried = None
        self.kids = None  # Set it in class Family ex: person.kids.
        self.nativeLanguage = None
        self.spokenLanguages = None  # List
        self.hobby = None
        self.job = None  # Class Job ex: person.job.salary

    def set_random(self, gender, nationality, age, country, city, native):
        if not nationality:
            nationality = nationalities.get_fake_nationality(country, city, native)
        elif nationality:
            nationality = nationalities.check_nationality(nationality, native)
        self.nationality = nationality

        if not age:
            age = person_data.age()
        self.age = age

        if not country:
            country = nationalities.get_fake_country(nationality, city, native)
        elif country:
            country = nationalities.check_country(country, native)
        self.country = country

        self.gender = person_data.get_gender(gender, self.country, native)

        if not city:
            pass
            city = nationalities.get_fake_city(nationality, self.country)
        elif city:
            city = nationalities.check_city(city)
        self.city = city

        self.height = person_data.get_height(self.age, self.gender, self.nationality)

    def to_json(self):  # Export not done
        pass

    def to_xml(self):  # Export not done
        pass

    def to_txt(self):  # Export not done
        pass


class Documents:
    def __init__(self):
        self.id = None
        self.creditCard = None
        self.driverLicense = None


class Parents:
    def __init__(self, gender: Union[int, str], nationality: str, age: int, country: str, city: str,
                 native: bool) -> None:
        self.gender = None  # MALE = 1, FEMALE = 2
        self.nationality = None
        self.age = None
        self.country = None
        self.city = None

        self.firstname = None
        self.lastname = None
        self.name = None
        self.bornMonth = None
        self.bornDay = None
        self.bornYear = None
        self.birthday = None
        self.isDead = None
        self.mother = None
        self.dad = None
        self.nativeLanguage = None
        self.spokenLanguages = None
        self.hobby = None
        self.job = None


class HomeAddress:
    def __init__(self) -> None:
        self.state = None
        self.zip = None
        self.street = None
        self.number = None

    def set_random(self, person):
        pass


class WorkAddress:
    def __init__(self, zip: int, city: str, street: str, number: int) -> None:
        self.zip: int = zip
        self.city: str = city
        self.street: str = street
        self.number: int = number


def random_person(gender: Union[int, str] = None,
                  nationality: str = None,
                  age: int = None,
                  country: str = None,
                  city: str = None,
                  native: bool = False) -> Person:
    person = Person(gender=gender, nationality=nationality, age=age, country=country, city=city, native=native)
    return person
