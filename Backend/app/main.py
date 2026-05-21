import os
from fastapi import FastAPI, Body, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
import random
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import time
from . import models
from . database import engine, SessionLocal
load_dotenv()
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Update this if your port is different
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependecy
def get_db()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Book(BaseModel):
    title: str
    author: str
    year: int
    price: float
    platform: str
    ispirated: bool=False
    link : str
connection = None
def connect_to_db():
    while True:
        global connection
        try:
            connection = psycopg2.connect(host = os.getenv("HOST"), database = os.getenv("DATABASE"), user=os.getenv("DBUSER"), password=os.getenv("MY_SECRET_PASSWORD"), cursor_factory=RealDictCursor)
            cursor = connection.cursor()
            print("Database connection successful")
            return cursor
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

cursor = connect_to_db()
@app.get("/")
async def root():
    a = random.random()
    if a > 0.5:
        value = "Greater than 0.500"
    else:
        value = "Less than 0.500"
    return {"status": "The Web API is Running.", "value": value}

@app.get("/random")
async def random_value(status_code=status.HTTP_200_OK):
    a = random.random()
    return {"value": a}



Books = [{"title":"American Psycho","author":"Bret Easton Ellis","year":1991,"price":9.99,"platform":"Amazon","ispirated":True,"link":"https://www.amazon.com/American-Psycho-Bret-Easton-Ellis/dp/0307949486"}]
@app.post("/book", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    try:
        connect_to_db()
        cursor.execute("""INSERT INTO books (title, author, year, price, platform, ispirated, link) VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                    (book.title, book.author, book.year, book.price, book.platform, book.ispirated, book.link))
        connection.commit()
        print(book.dict())
    except Exception as e:
        print(f"Error inserting book: {e}")
        return {"message": "Error inserting book"}
    return {"message": "Book created successfully", "book": book}

@app.delete("/deletebook")
async def delete_book(title:str = Body(...)):
    global Books
    for book in Books:
        if book["title"] == title:
            Books.remove(book)
            print(Books)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}

@app.get("/book")
def get_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print(books)
    return {"books": books}
@app.get("/book/{id}")
def get_book_by_id(id: int, response: Response):
    cursor.execute("""SELECT * FROM books where ID = %s """,(id,))
    book = cursor.fetchone()
    if book is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Book with this Id doesn't exist"}
    return {"books":book}


@app.get("/notsupposedtobesearched/{id}")
def naughty_user(id: int, response: Response  ):
    if id == 69:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden: You are not allowed to access this resource.")
    response.status_code = status.HTTP_403_FORBIDDEN
    return {"message":"You are a naughty user, you are not supposed to search for this page!"}
@app.delete("/book/{id}")
def get_book_by_id(id: int, response: Response):
    cursor.execute("""DELETE FROM books where ID = %s returning * """,(id,))
    book = cursor.fetchone()
    connection.commit()
    if book is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Book with this Id doesn't exist"}
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)