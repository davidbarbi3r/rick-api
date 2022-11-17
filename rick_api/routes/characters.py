from fastapi import APIRouter

router = APIRouter(prefix="/characters", tags=["Characters"])

@router.get("/")
def get_characters():
    pass 