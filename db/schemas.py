from pydantic import BaseModel, Field


class AuthorBase(BaseModel):

    id:int
    bio:str
    name:str
    
    class Config:
        from_attributes = True

class BoocksBase(BaseModel):

    id:int
    title:str
    pages:int
    author_id:int

    class Config:
        from_attributes = True
