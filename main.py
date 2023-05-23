from fastapi import FastAPI
from app.routers import urls

app = FastAPI()

# Include the router
app.include_router(urls.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
