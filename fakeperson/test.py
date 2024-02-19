from fakeperson import random_person

person = random_person(nationality="DEU", native=True)
print(f'Gender: {person.gender}')
print(f'Nationality: {person.nationality}')
print(f'Age: {person.age}')
print(f'Country: {person.country}')
print(f'City: {person.city}')
