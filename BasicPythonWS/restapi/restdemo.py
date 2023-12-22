from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# database managed entity
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/") 
def root(): 
	return {"message": "Hello World"}

@app.get("/greet") 
def root(): 
	return {"message": "Hello There!!"}

@app.get("/profile/{username}") 
def root(username:str):
	profile = {
		'name':username,
		'city': username+' City'
    } 
	return profile

@app.post("/items/")
def create_item(item: Item):
    print('to insert item in database')
    return item

fake_items_db = [{"item_name": "Foo"}, 
                 {"item_name": "Bar"}, 
                 {"item_name": "Baz"},
                 {"item_name": "oof"},
                 {"item_name": "Poo"},
                 {"item_name": "Pap"},
                 {"item_name": "Nee"},
                 {"item_name": "Tee"},
                 {"item_name": "Rop"},
                 {"item_name": "Baa"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit] #slicing

