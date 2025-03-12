from fastapi import FastAPI

from routes.base_router import router as home_router
from routes.books import router as books_router

app = FastAPI()
app.include_router(home_router)
app.include_router(books_router)
