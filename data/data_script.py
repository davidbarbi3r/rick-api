import json
from database.database import Database


characters_data = open("data/rick_morty-characters_v1.json").read()
characters_obj = json.loads(characters_data)

episodes_data = open("data/rick_morty-episodes_v1.json").read()
episodes_obj = json.loads(episodes_data)


for character in characters_obj:
    id_char = character.get("id")
    name = character.get("name")
    status = character.get("status")
    species = character.get("species")
    type_char = character.get("type")
    gender = character.get("gender")
    insert_query = "INSERT INTO characters(id,name,status,species,type,gender) VALUES(%s, %s, %s, %s, %s, %s)"
    Database.query(insert_query, (id_char, name, status, species, type_char, gender))

for episode in episodes_obj:
    id_ep = episode.get("id")
    name = episode.get("name")
    air_date = episode.get("air_date")
    episode = episode.get("episode")
    insert_query = "INSERT INTO episodes(id, name, air_date, episode) VALUES(%s, %s, %s, %s)"
    Database.query(insert_query, (id_ep, name, air_date, episode))

for character in characters_obj:
    for episode in episodes_obj:
        id_char = character.get("id")
        id_ep = episode.get("id")
        insert_query = "INSERT INTO characters_episodes(id_characters, id_episodes) VALUES(%s, %s)"
        Database.query(insert_query, (id_char, id_ep))

Database.commit()
Database.close()
