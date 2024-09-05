from fastapi import FastAPI
from api.book_api import book_router
from api.user_api import user_router
from api.bookcrossing_api import bookcrossing_router
from db import Base, engine

app = FastAPI(docs_url="/")
Base.metadata.create_all(engine)

app.include_router(book_router)
app.include_router(user_router)
app.include_router(bookcrossing_router)
