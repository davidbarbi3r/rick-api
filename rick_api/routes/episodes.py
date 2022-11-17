from fastapi import APIRouter

router = APIRouter(prefix="/episodes", tags=["Episodes"])

@router.get("/")
def get_episodes():
    pass