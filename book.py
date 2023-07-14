import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api
from datetime import datetime
from utilizies.jsonconverter import databaseJsonConverter
from authen import token_required


bok=api.model('Bok', {
    'venue_id': fields.Integer(required=True, description='venue ID'),
    'user_id': fields.Integer(required=True, description='user ID'),
    'booking_date': fields.Date(required=True,description='venue date (YYYY-MM-DD)'),
    'booking_time': fields.Date(required=True,description='venue time (HH:MM:SS)'),
    'rating': fields.Integer(required=True,description='The task details'),
    'payment_amount': fields.Integer(required=True,description='The task details'), 
    
     })

name_space=api.namespace('Booking','all about booking fustsal')
@cross_origin
@name_space.route("/CRUD",methods=['POST'])
@name_space.route('/CRUD/<int:booking_id>',methods=['GET','PUT','DELETE'])
class bookCRUD(Resource):
    @api.expect(bok)
    @token_required
    @api.doc(params={'venue_id': 'As integer','user_id ': 'As integer','booking_date': 'As integer', 'booking_time':'As integer','image':'As integer','rating':'As string','payment_amount':'As integer','day':'As integer'})
    
    def post(self):
        cur2 = dbconnection.cursor()
        try:
            venue_id = request.json['venue_id']
            user_id = request.json['user_id']
            booking_date = request.json['booking_date']
            booking_time = request.json['booking_time']
            rating = request.json['rating']
            payment_amount = request.json['payment_amount']
            cur2.execute("INSERT INTO booking(venue_id,user_id,booking_date, booking_time, rating, payment_amount) values( %s, %s, %s, %s,%s,%s)", (venue_id,user_id,booking_date, booking_time,rating, payment_amount,))
            dbconnection.commit()
            if cur2.rowcount > 0:
                return json.dumps({'msg': 'Successfully', 'status_code': '200'})
            else:
                return json.dumps({'msg': 'Already', 'status_code': '400'})
        except Exception as e:
            raise e
        finally:
            cur2.close()
            dbconnection.close()

    @token_required
    @api.expect(bok)
    @api.doc(params={'venue_id': 'As integer','user_id': 'As integer','booking_date': 'As integer', 'booking_time':'As integer','rating':'As string','payment_amount':'As integer'})
    def put(self, booking_id=0):
        cur3 = dbconnection.cursor()
        try:
            venue_id = request.json['venue_id']
            user_id = request.json['user_id']
            booking_date = request.json['booking_date']
            booking_time = request.json['booking_time']
            rating = request.json['rating'] 
            payment_amount = request.json['payment_amount']
            cur3.execute("UPDATE booking SET venue_id=%s,user_id=%s,booking_date=%s, booking_time=%s, rating=%s, payment_amount=%s WHERE booking_id=%s", (venue_id,user_id,booking_date, booking_time, rating, payment_amount, booking_id,))
            dbconnection.commit()
            return json.dumps({'msg': 'Update successful', 'status_code': '200'})
        except Exception as ex:
            raise ex
        finally:
            cur3.close()
            dbconnection.close()



    @token_required
    def delete(self, booking_id=0):
        cur4 = dbconnection.cursor()
        try:
            cur4.execute("UPDATE booking SET delete_flag = 1 WHERE booking_id = %s", (booking_id,))
            dbconnection.commit()
            return json.dumps({'msg': 'Delete successful', 'status_code': 200}) 
        except Exception as ex:
            raise ex
        finally:
            cur4.close()
            dbconnection.close()
       

        
date_model = api.model('Date', {
    'datefrom': fields.Date(required=True, description='Venue date'),
    'dateto': fields.Date(required=True, description='Venue time')
})
name_space3=api.namespace('Getdate','all about booking search fustsal')
@cross_origin
@name_space3.route('/get_booking',methods=['POST'])
class dateCRUD(Resource):
    @api.expect(date_model)
    @token_required
    @api.doc(params={'datefrom': 'As date', 'dateto': 'As date'})
    
    def post(self):
        cur5 = dbconnection.cursor()
        try:
            datefrom = request.json['datefrom']
            dateto = request.json['dateto']
            cur5.execute("SELECT booking_date FROM booking WHERE booking_date BETWEEN %s AND %s", (datefrom, dateto,))
            data = databaseJsonConverter(cur5)
            if data:
                return ({'msg': data, 'status_code': 200})
            else:
                return ({'msg': 'No bookings found', 'status_code': 200})

        except Exception as ex1:
            raise ex1

        finally:
            cur5.close()
            dbconnection.close()
        

        

# name_space2=api.namespace('Booking Search','all about booking search fustsal')
# @cross_origin
# @name_space2.route('/get_booking_by_date',methods=['POST'])
# class searchCRUD(Resource):
#     @api.expect(bok)
#     @api.doc(params={'booking_date': 'As integer', 'booking_time':'As integer','rating':'As string','payment_amount':'As integer'})
#     def post(self):
#         cur6 = dbconnection.cursor()
#         try:
#             booking_date = request.json['booking_date']
#             booking_time = request.json['booking_time']
#             rating = request.json['rating']
#             payment_amount = request.json['payment_amount']
#             search_date = request.json["search_date"]
            
#             cur6.execute("SELECT * FROM booking WHERE booking_date = %s", (search_date,))
#             result = cur6.fetchone()
            
#             match_date = []
#             if result and result['booking_date'] == search_date:
#                 match_date.append(result)

#             if len(match_date) > 0:
#                 return json.dumps({'message': 'The futsal date is available', 'status_code': '200'})
#             else:
#                 return json.dumps({'message': 'The futsal date is not available', 'status_code': '400'})
#         except Exception as ex2:
#             raise ex2
#         finally:
#             cur6.close()
#             dbconnection.close()
            

