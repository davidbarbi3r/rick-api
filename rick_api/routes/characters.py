from fastapi import APIRouter
from ..main import *

router = APIRouter(prefix="/characters", tags=["Characters"])


@router.get("/")
def get_characters():
    data = db.get("*", "characters", join=False)
    return data

@router.get("/ep")
def get_characters_with_ep():
    data = db.get("*", "characters_episodes", table_join="characters",
                  join_key1="characters_episodes.id_characters", join_key2="characters.id")
    return data

# Pour mémoire de ma requete qui fonctionne
# SELECT *
# FROM characters_episodes
# INNER JOIN characters
# on characters_episodes.id_characters  =  characters.id
# order by id_characters ;
