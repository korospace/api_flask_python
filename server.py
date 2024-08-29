# Core
import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# Route
from book.route import book_route

def create_app():
    # App initiation
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    api = Api(app=app)

    # Route initiation
    book_route(api=api)

    with app.app_context():
        return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
