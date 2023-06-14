import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api

price = api.model('FutsalPrice', {
    'id': fields.Integer(required=True, description='Price ID'),
    'day': fields.String(required=True, description='Day of the week'),
    'time': fields.String(required=True, description='Time slot'),
    'price': fields.String(required=True, description='Price')
})
# futsal_prices = [
#     {'day':'day','time': 'Morning', 'price': 'Rs. 500/-'},
#     {'day':'day','time': 'Daytime', 'price': 'Rs. 800/-'},
#     {'day':'day','time': 'Evening', 'price': 'Rs. 1000/-'},
#     {'day':'day','time': 'Night', 'price': 'Rs. 1200/-'}
# ]

name_space2=api.namespace('Price','all about booking price futsal')
@cross_origin
@name_space2.route('/get_booking_by_price',methods=['POST'])
class priceCRUD(Resource):
    @api.doc(params={'booking_price': 'As integer', 'time':'As integer','day':'As integer','price':'As string'})
    def post(self):
        day=request.json['day']
        time=request.json['time']
        price=request.json['price']
        day=request.json['day']
        cur1 = dbconnection.cursor()
        cur1.execute("INSERT INTO futsal_prices (day,time, price) VALUES (%s, %s, %s)",(day,time,price,))
        values = (new_price['day'], new_price['time'], new_price['price'])
        cur1.execute(values)
        dat1 = cur1.fetchone()
        if dat1:
            return {'message': 'Price added successfully','status_code':'200'}
        else:
            return {'message': 'failed added successfully','status_code':'400'}


    def get(self):
        cur2 = dbconnection.cursor()
        cur2.execute("SELECT * FROM prices")
        dat2 = cur2.fetchone()
        dbconnection.commit()
        if dat2:
            return json.dumps({'msg':'Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Failed','status_code':'400'})
        cur.close()

     
        