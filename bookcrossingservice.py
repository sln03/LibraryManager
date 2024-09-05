from db import get_db
from db.models import Bookcrossing, Book, User


def issue_book_db(book: int, user: int, period: str):
    with next(get_db()) as db:
        book = db.query(Book).filter_by(book_id=book).first()
        user = db.query(User).filter_by(user_id=user).first()
        issuing = Bookcrossing(book=book, user=user, period=period)
        db.add(issuing)
        db.commit()
        return "Успешно выдано"


def return_book_db(book: int, user: int):
    with next(get_db()) as db:
        book = db.query(Book).filter_by(book_id=book).first()
        user = db.query(User).filter_by(user_id=user).first()
        returning = Bookcrossing(book_id=book, user_id=user)
        db.add(returning)
        db.commit()
        return "Успешно возвращено"
