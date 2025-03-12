# routes/books.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/books")
async def list_books():
    return {"message": "List of Books"}


@router.get("/books/{book_id}")
async def get_book(book_id: int):
    return {"message": f"Book {book_id}"}
