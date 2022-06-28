from urllib import response
from flask import (
    Flask,
    abort
)
from models import setup_db, Register, Catalogo, Categoria
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS, POST, PATCH, DELETE')
        return response

    @app.route('/')
    def index():
        return'hola'    


    
    return app

