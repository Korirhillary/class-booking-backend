from pydantic import BaseModel

class LecturehallSchema(BaseModel):
    Title:str
    image:str
    description:str
    price:str
    date:str