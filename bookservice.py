from db import get_db
from db.models import Book


def add_book_db(book_id, title, author, jenre, public_date, amount):
    with next(get_db()) as db:
        new_card = Book(book_id=book_id, title=title, author=author,
                        jenre=jenre, public_date=public_date, amount=amount)
        db.add(new_card)
        db.commit()
        return True


def delete_exact_book_db(book_id):
    with next(get_db()) as db:
        delete_book = db.query(Book).filter_by(book_id=book_id).first()
        if delete_book:
            db.delete(delete_book)
            db.commit()
            return True
        return False


def get_exact_book_db(book_id):
    with next(get_db()) as db:
        exact_book = db.query(Book).filter_by(book_id=book_id).first()
        if exact_book:
            return exact_book
        return False


def checker_book_info_db(book_id, title):
    with next(get_db()) as db:
        checker = db.query(Book).filter_by(book_id=book_id, book_title=title).first()
        if checker:
            return True
        return False
