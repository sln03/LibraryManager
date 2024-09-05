from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    surname = Column(String(55), nullable=False)
    name = Column(String(55), nullable=False)
    user_photo = Column(String)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_city = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now)


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    public_date = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)


class Bookcrossing(Base):
    __tablename__ = "bookcrossing"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user = Column(Integer, ForeignKey("users.user_id"))
    book = Column(Integer, ForeignKey("books.book_id"))
    period = Column(String, nullable=False)
    issue_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime, default=datetime.now)

    user_fk = relationship(User, lazy="subquery")
    book_fk = relationship(Book, lazy="subquery")
