from pydantic import BaseModel

class LecturehallSchema(BaseModel):
    Title:str
    image:str
    description:str
    price:str
    

class BooklecturehallSchema(BaseModel):
    first_name:str
    last_name:str
    phone_number:str
    date:str

class UserSchema(BaseModel):

    lecturehall_id:int
    user_id:int