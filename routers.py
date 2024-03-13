from fastapi import APIRouter
from scrapping import scrapping_broadcast

router = APIRouter()

@router.get('/scrapping-broadcast/')
def broadcast():
    return scrapping_broadcast()