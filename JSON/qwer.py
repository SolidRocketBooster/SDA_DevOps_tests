import json

with open('data.json') as file_j:
    data = file_j.read()

def show_hero(json_hero):
    dic_hero = json.loads(json_hero)
    ch_class = dic_hero[0]['character_class']['name']
    name = dic_hero[0]['name']
    hp = dic_hero[0]['hp']
    strength = dic_hero[0]['character_class']['strength']
    armour = dic_hero[0]['armour']
    print(f"Class: {ch_class}, Name: {name}, HP: {hp}, Strength: {strength}, Armour: {armour}")


show_hero(data)
