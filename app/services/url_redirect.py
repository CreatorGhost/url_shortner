from app.db import database
from fastapi import HTTPException

async def redirect_to_url(redirect_in):
    # Retrieve the original URL from the database
    url_doc = await database["urls"].find_one({"short_url": redirect_in.url})

    if url_doc is None:
        raise HTTPException(status_code=404, detail="URL not found")

    # Return a redirect response
    return {"url": url_doc["original_url"]}
