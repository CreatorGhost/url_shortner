from fastapi import APIRouter
from app.models.urls import UrlIn, UrlOut, UrlRedirectIn, UrlClicks
from app.services import url_shortener, url_redirect

router = APIRouter()

@router.post("/hash-url", response_model=UrlOut)
async def create_hash_url(url_in: UrlIn):
    return await url_shortener.create_short_url(url_in)

@router.get("/redirect")
async def redirect_url(hashed_url: str):
    return await url_redirect.redirect_to_url(hashed_url)

@router.get("/clicks", response_model=UrlClicks)
async def get_clicks(hashed_url: str):
    return await url_shortener.get_clicks(hashed_url)
