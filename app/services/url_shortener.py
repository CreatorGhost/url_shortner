from pyshorteners import Shortener
from app.db import database
from fastapi import HTTPException


async def create_short_url(url_in):
    # Use pyshorteners to generate a shortened URL
    shortener = Shortener()
    short_url = shortener.tinyurl.short(url_in.url)

    # Store the original URL and the shortened URL in the database
    url_doc = {
        "original_url": url_in.url,
        "short_url": short_url,
        "single_use": url_in.single_use,
    }

    await database.database.urls.insert_one(url_doc)

    return {"url": short_url}


async def get_clicks(short_url):
    url_doc = await database.database.urls.find_one({"short_url": short_url})

    if url_doc is None:
        raise HTTPException(status_code=404, detail="URL not found")

    return {"click_count": url_doc["click_count"]}
