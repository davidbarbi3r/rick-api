from fastapi import APIRouter
from ..main import *

router = APIRouter(prefix="/episodes", tags=["Episodes"])

@router.get("/")
def get_episodes():
    data = db.get("*", "episodes", join=False)
    return data

@router.get("/char")
def get_episodes_with_char():
    data = db.get("*", "characters_episodes", table_join="episodes",
                  join_key1="characters_episodes.id_episodes", join_key2="episodes.id")
    return data

# Pour mémoire de ma requete qui fonctionne
# SELECT *
# FROM characters_episodes
# INNER JOIN episodes
# on characters_episodes.id_episodes  =  episodes.id
# order by id_episodes ;
