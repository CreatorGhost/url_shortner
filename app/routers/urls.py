from fastapi import APIRouter
from app.models import UrlIn, UrlOut, UrlRedirectIn
from app.services import url_shortener, url_redirect

router = APIRouter()

@router.post("/hash-url", response_model=UrlOut)
async def create_hash_url(url_in: UrlIn):
    return await url_shortener.create_short_url(url_in)

@router.get("/{hashed_url}")
async def redirect_url(redirect_in: UrlRedirectIn):
    return await url_redirect.redirect_to_url(redirect_in)
