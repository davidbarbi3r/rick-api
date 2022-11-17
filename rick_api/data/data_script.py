import sys
sys.path.append('/home/gnark/projects/rick-api')

import json
from rick_api.infra.database import Database

db = Database()

characters_data = open("rick_api/data/rick_morty-characters_v1.json").read()
characters_obj = json.loads(characters_data)

episodes_data = open("rick_api/data/rick_morty-episodes_v1.json").read()
episodes_obj = json.loads(episodes_data)


for character in characters_obj:
    id_char = character.get("id")
    name = character.get("name")
    status = character.get("status")
    species = character.get("species")
    type_char = character.get("type")
    gender = character.get("gender")
    db.insert("characters", id=id_char, name=name, status=status, species=species, type=type_char, gender=gender)

for episode in episodes_obj:
    id_ep = episode.get("id")
    name = episode.get("name")
    air_date = episode.get("air_date")
    label = episode.get("episode")
    db.insert("episodes", id=id_ep, name=name, air_date=air_date, episode=label)

    for id_character in episode.get("characters"):
        db.insert("characters_episodes", id_characters=id_character, id_episodes=id_ep)


db.close()
