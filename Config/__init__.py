from flask import Flask
from flask_restx import Api
from flask_cors import CORS
import mysql.connector

dbconnection = mysql.connector.connect(host='localhost',
                                         database='data',
                                         user='root',
                                         password='')
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app, version='1.0', title='Fustal',
    description='Futsal API',
    )
cors = CORS(app)

from book import *
from user import *   
from news import * 
from owner import * 
from payment import * 
from venue import*
from authen import*
from prices import*