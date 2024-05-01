from fastapi import Body, FastAPI

app=FastAPI()

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "year": 1925
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "year": 1813
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "year": 1951
    }
]



#static parameter 
@app.get("/")
def index():
    return "welcome to demo website"

@app.get("/books")
def read_all_books():
    return books

#dynamic path parameter 
@app.get("/books/{book_title}")
def read_book(book_title: str):
    try:
        for book in books:
            if book.get('title').casefold()==book_title.casefold():
                return book
    except Exception as e:
        return e

#query parameter
@app.get("/books/")
async def read_category_by_query(category: str):
    book_to_return=[]
    for book in books:
        if book.get('genre').casefold()==category.casefold():
            book_to_return.append(book)
    
    return book_to_return

#we can have path and category together
@app.get("/books/{author}/")
def read_author_category_by_query(author: str,category: str):
    books_to_return=[]
    for book in books:
        if (book.get('author').casefold()==author.casefold()) and (book.get('genre').casefold()==category.casefold()):
            books_to_return.append(book)
    return books_to_return


#post api request
#post api request is for saving the data or creating the request.
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    books.append(new_book)

#put request
#used when you need to update already saved data

@app.put("/books/update_books")
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        if books[i].get('title')==updated_book.get('title'):
            books[i]=updated_book