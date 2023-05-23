from pydantic import BaseModel,Field

class UrlIn(BaseModel):
    url: str
    single_use: bool = Field(False,required=False)

class UrlOut(BaseModel):
    url: str

class UrlRedirectIn(BaseModel):
    url: str

class UrlClicks(BaseModel):
    click_count: int
