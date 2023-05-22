from pydantic import BaseModel

class UrlIn(BaseModel):
    url: str

class UrlOut(BaseModel):
    url: str

class UrlRedirectIn(BaseModel):
    url: str
