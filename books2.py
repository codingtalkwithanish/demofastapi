from fastapi import Body, FastAPI
#pydantic comes preinstalled with fastapi
#and helps in data validation and modelling
from pydantic import BaseModel,Field
app=FastAPI()

class Book:
    id: int 
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating


class BookRequest(BaseModel):
    id:int
    title:str = Field(min_length=3)
    author:str =Field(min_length=3)
    description:str =Field(min_length=5,max_length=100)
    rating:int =Field(gt=0,lt=6)

BOOKS=[
    Book(1,'let us c','kanitkar','introdution to c language',5),
    Book(2,'roof on the wall','ruskin bond','drama',5),
    Book(3,'first head java','Author 1','introdution to java language',3),
    Book(4,'hp1','Author 2','introdution to hp1',2),
    Book(5,'hp2','Author 3','introdution to hp2',1),
    Book(6, 'hp3','  Author 4','introdution to hp3',4)
]

@app.get("/")
async def index():
    return "welcome to home page"

@app.get("/books")
async def read_all_books():
    return BOOKS

#post request without pydantic
# @app.post("/books/create_book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)

#post request with pydantic
@app.post("/books/create_book")
async def create_book(book_request:BookRequest):
    new_book= Book(**book_request.model_dump()) 
    BOOKS.append(find_book_id(new_book))
    
def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1
    else:
        book.id=1
    return book