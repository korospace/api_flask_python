from flask_restful import Api
from book.controller import GetBook

def book_route(api: Api):
    api.add_resource(GetBook, "/api/book/get")
