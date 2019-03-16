from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open('heros.yml', 'r') as file_handler:
    heroes = load(file_handler, Loader=Loader)

for race, hero in heroes.items():
    race = race.capitalize()
    name = hero['name']
    ch_class = hero['class']
    hp = hero['hp']
    armour = hero['armour']
    skills = ', '.join(hero['skills'])
    print(f'Class: {ch_class}, Race: {race}, Name: {name}, '
          f'HP: {hp}, Armour: {armour}, Skills: {skills}')
