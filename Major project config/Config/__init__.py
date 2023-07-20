from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from werkzeug.middleware.proxy_fix import ProxyFix


appauthorizations={
    'apikey':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

cors = CORS(app)

api = Api(app, version='1.0', title='Futsal',security='apikey',
    description='Futsal API', authorizations=appauthorizations
    )



# from book import *
from user import *   
# from news import * 
# from owner import * 
# from payment import * 
from venue import*
# from image import*