from app.db import database
from fastapi import HTTPException


async def redirect_to_url(hashed_url: str):
    url_doc = await database.database.urls.find_one({"short_url": hashed_url})

    if url_doc is None:
        raise HTTPException(status_code=404, detail="URL not found")

    # Increment click count
    await database.database.urls.update_one(
        {"short_url": hashed_url}, {"$inc": {"click_count": 1}}
    )

    # If the URL is single-use, delete it after redirecting
    if url_doc["single_use"]:
        await database.database.urls.delete_one({"short_url": hashed_url})

    return {"url": url_doc["original_url"]}
