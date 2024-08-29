# core import
from flask import Response
from flask_restful import Resource
from flask import request, make_response

# service import
from book.service import get_book

class GetBook(Resource):
    @staticmethod
    def get() -> Response:
        response, status = get_book(request)

        return make_response(response, status)