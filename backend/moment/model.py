import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship, sessionmaker

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
from backend import db


# Base = declarative_base()


# We will add classes here
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), nullable=False)
    author = db.Column(String(250), nullable=False)
    genre = db.Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'id': self.id,
        }


# el = Book(title="Test")
# db.session.add(el)


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
        }

    # def __repr__(self):
    #     return {
    #         'id': self.id,
    #         'username': self.username,
    #         'email': self.email,
    #         'password_hash': self.password_hash,
    #     }

# # Creates a create_engine instance at the bottom of the file
# engine = create_engine('sqlite:///backend/data/books-collection.db')
# Base.metadata.create_all(engine)
#
# # Connect to Database and create database session
# engine = create_engine('sqlite:///backend/data/books-collection.db')
# Base.metadata.bind = engine
#
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# # landing page that will display all the books in our database
# # This function operate on the Read operation.
# @app.route('/books')
# def showBooks():
#     books = session.query(Book).all()
#     return render_template("books.html", books=books)
#
#
# # This will let us Create a new book and save it in our database
# @app.route('/books/new/', methods=['GET', 'POST'])
# def newBook():
#     if request.method == 'POST':
#         newBook = Book(title=request.form['name'],
#                        author=request.form['author'],
#                        genre=request.form['genre'])
#         session.add(newBook)
#         session.commit()
#         return redirect(url_for('showBooks'))
#     else:
#         return render_template('newBook.html')
#
#
# # This will let us Update our books and save it in our database
# @app.route("/books/<int:book_id>/edit/", methods=['GET', 'POST'])
# def editBook(book_id):
#     editedBook = session.query(Book).filter_by(id=book_id).one()
#     if request.method == 'POST':
#         if request.form['name']:
#             editedBook.title = request.form['name']
#             return redirect(url_for('showBooks'))
#     else:
#         return render_template('editBook.html', book=editedBook)
#
#
# # This will let us Delete our book
# @app.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
# def deleteBook(book_id):
#     bookToDelete = session.query(Book).filter_by(id=book_id).one()
#     if request.method == 'POST':
#         session.delete(bookToDelete)
#         session.commit()
#         return redirect(url_for('showBooks', book_id=book_id))
#     else:
#         return render_template('deleteBook.html', book=bookToDelete)
#
#
# """
# api functions
# """
# from flask import jsonify, request
#
#
# def get_books():
#     books = session.query(Book).all()
#     return jsonify(books=[b.serialize for b in books])
#
#
# def get_book(book_id):
#     books = session.query(Book).filter_by(id=book_id).one()
#     return jsonify(books=books.serialize)
#
#
# def makeANewBook(title, author, genre):
#     addedbook = Book(title=title, author=author, genre=genre)
#     session.add(addedbook)
#     session.commit()
#     return jsonify(Book=addedbook.serialize)
#
#
# def updateBook(id, title, author, genre):
#     updatedBook = session.query(Book).filter_by(id=id).one()
#     if not title:
#         updatedBook.title = title
#     if not author:
#         updatedBook.author = author
#     if not genre:
#         updatedBook.genre = genre
#     session.add(updatedBook)
#     session.commit()
#     return 'Updated a Book with id %s' % id
#
#
# def deleteABook(id):
#     bookToDelete = session.query(Book).filter_by(id=id).one()
#     session.delete(bookToDelete)
#     session.commit()
#     return 'Removed Book with id %s' % id
#
#
# @app.route('/booksApi', methods=['GET', 'POST'])
# def booksFunction():
#     if request.method == 'GET':
#         return get_books()
#     elif request.method == 'POST':
#         title = request.args.get('title', '')
#         author = request.args.get('author', '')
#         genre = request.args.get('genre', '')
#         return makeANewBook(title, author, genre)
#
#
# @app.route('/booksApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# def bookFunctionId(id):
#     if request.method == 'GET':
#         return get_book(id)
#
#     elif request.method == 'PUT':
#         title = request.args.get('title', '')
#         author = request.args.get('author', '')
#         genre = request.args.get('genre', '')
#         return updateBook(id, title, author, genre)
#
#     elif request.method == 'DELETE':
#         return deleteABook(id)
