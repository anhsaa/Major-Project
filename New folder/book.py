import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api


bok=api.model('Bok', {
    'booking_date': fields.Date(required=True,description='venue date (YYYY-MM-DD)'),
    'booking_time': fields.Date(required=True,description='venue time (HH:MM:SS)'),
    'rating': fields.String(required=True,description='The task details'),
    'payment_amount': fields.String(required=True,description='The task details'), 
    
     })

name_space=api.namespace('Booking','all about booking fustsal')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:booking_id>',methods=['GET'])
class bookCRUD(Resource):
    @api.expect(bok)
    @api.doc(params={'booking_date': 'As integer', 'booking_time':'As integer','image':'As integer','rating':'As string','payment_amount':'As integer','day':'As integer'})
    
    def post(self):
        booking_date = request.json['booking_date']
        booking_time = request.json['booking_time']
        rating = request.json['rating']
        payment_amount = request.json['payment_amount']
        cur2 = dbconnection.cursor()
        cur2.execute("INSERT INTO booking(booking_date, booking_time, rating, payment_amount) values( %s, %s, %s, %s)", (booking_date, booking_time,rating, payment_amount,))
        dbconnection.commit()
        if cur2.rowcount > 0:
            return json.dumps({'msg': 'Successfully', 'status_code': '200'})
        else:
            return json.dumps({'msg': 'Already', 'status_code': '400'})


    def put(self, booking_id=0):
        booking_date = request.json['booking_date']
        booking_time = request.json['booking_time']
        rating = request.json['rating']
        payment_amount = request.json['payment_amount']
        cur3 = dbconnection.cursor()
        cur3.execute("UPDATE booking SET booking_date=%s, booking_time=%s, rating=%s, payment_amount=%s,  WHERE id=%s", (booking_date, booking_time, rating, payment_amount, booking_id,))
        dbconnection.commit()
        update_booking_id = cur3.lastrowid
        if update_booking_id:
            return json.dumps({'msg': 'Update successfully', 'status_code': '200'})
        else:
            return json.dumps({'msg': 'Failed to update', 'status_code': '400'})


    def delete(self, booking_id=0):
        cur4 = dbconnection.cursor()
        cur4.execute("UPDATE booking SET delete_flag = 0 WHERE booking_id = {booking_id}")
        dbconnection.commit()
        dbconnection.delete(booking_id)
        if cur4.rowcount > 0:
            return json.dumps({'msg': 'Delete successful', 'status_code': 200})
        else:
            return json.dumps({'msg': 'Already deleted', 'status_code': 400})

    def get(self, id=0):
        cur5 = dbconnection.cursor()
        cur5.execute("SELECT * FROM booking ")
        dat5 = cur5.fetchone()
        dbconnection.commit()
        if dat5:
            dat5['booking_date'] = dat5['booking_date'].strftime("%Y-%m-%d")
            return json.dumps({'msg': dat5, 'status_code': '200'})
        else:
            return json.dumps({'msg': 'Failed', 'status_code': '400'})


        

name_space2=api.namespace('Booking Search','all about booking search fustsal')
@cross_origin
@name_space2.route('/get_booking_by_date',methods=['POST'])
class dateCRUD(Resource):
    @api.doc(params={'booking_date': 'As integer', 'booking_time':'As integer','rating':'As string','payment_amount':'As integer'})
    
    def post(self):
        booking_date = request.json['booking_date']
        booking_time = request.json['booking_time']
        rating = request.json['rating']
        payment_amount = request.json['payment_amount']
        search_date = request.json["search_date"]
        cur6 = dbconnection.cursor()
        cur6.execute("SELECT * FROM booking WHERE booking_date = %s", (search_date,))
        result = cur6.fetchone()
        dbconnection.commit()
        dbconnection.close()
        match_date = []
        if result and result['booking_date'] == search_date:
            match_date.append(result)

        if len(match_date) > 0:
            return json.dumps({'message': 'The futsal date is available', 'status_code':'200'})
        else:
            return json.dumps({'message': 'The futsal date is not available', 'status_code':'400'})