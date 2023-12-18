from fastapi import FastAPI
from schemas import LecturehallSchema
app = FastAPI()

#define a route
@app.get('/lecturehalls')
def index():
    return{"Message":"welcome to my first aPi"}

@app.get('/lecturehalls/{lecturehall_id}')
def sunday():
    return[]

# create a lecturehall
@app.post('/lecturehalls')
def create(lecturehall:LecturehallSchema):
    return{"Message":"Happy New year 2024"}

# update Lecturehall
@app.patch('/lecturehalls/{lecturehall_id}')
def updated_event(lecturehall_id:int):
    return{"message":f"{lecturehall_id}created successfully"}
 
 #delete lecturehall
@app.delete('/lecturehalls/{lecturehall_id}')
def delete_lecturehall(lecturehall_id:int):
    return{"message":f"{lecturehall_id} deleted successfully"}

