from pyshorteners import Shortener
from app.db import database

async def create_short_url(url_in):
    # Use pyshorteners to generate a shortened URL
    shortener = Shortener()
    short_url = shortener.tinyurl.short(url_in.url)

    # Store the original URL and the shortened URL in the database
    url_doc = {"original_url": url_in.url, "short_url": short_url}
    await database["urls"].insert_one(url_doc)

    return {"url": short_url}
