from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api


bok=api.model('Bok', {
    'fustal_name': fields.String(required=True, description='The task details'),
    'email': fields.String(required=True, description='The task details'),
    'phone': fields.String(required=True,description='The task details'),
    'booking_data': fields.String(required=True,description='The task details'),
    'booking_time': fields.String(required=True,description='The task details'),
    'checking_data': fields.String(required=True,description='The task details'),
    'checking_time': fields.String(required=True,description='The task details'), 
     })
name_space=api.namespace('Booking','all about users')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:id>',methods=['GET'])
class bookCRUD(Resource):
    @api.expect(bok)
    @api.doc(params={'name': 'As String','email':'As string','phone':'As integer','booking_date': 'As integer', 'booking_time':'As integer','checking_data':'As integer','checking_time':'As integer'})
    def post(self):
        futsal_name=request.json['futsal_name']
        email=request.json['email']
        phone=request.json['phone']
        booking_data=request.json['booking_data']
        booking_time=request.json['booking_time']
        checking_data=request.json['checking_data']
        checking_time=request.json['checking_time']
        cur2 = dbconnection.cursor()
        cur2.execute("INSERT INTO booking(fustal_name,email, phone,booking_data,booking_time,checking_data,checking_time) values(%s,%s,%s,%s,%s,%s,%s)",(futsal_name,email,phone,booking_data,booking_time,checking_data,checking_time,))
        dat1 = cur2.fetchone()
        if dat1:
            return json.dumps({'msg':'Booking Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Already Booked','status_code':'400'})
        cur.close() # closing a cursor

    def put(self,booking_id=0):
    
        futsal_name=request.json['futsal_name']
        email=request.json['email']
        phone=request.json['phone']
        booking_data=request.json['booking_data']
        booking_time=request.json['booking_time']
        checking_data=request.json['checking_data']
        checking_time=request.json['checking_time']
        cur3 = dbconnection.cursor()
        cur3.execute("UPDATE booking SET fustal_name=%s,email=%s, phone=%s,booking_data=%s,booking_time=%s,checking_data=%s,checking_time=%s WHERE booking_id=%s ",(futsal_name,email,phone,booking_data,booking_time,checking_data,checking_time,booking_id,))
        dat2 = cur3.fetchone()
        if dat2:
            return json.dumps({'msg':'update Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Failed to update','status_code':'400'})
        cur.close() # closing a cursor

    def get(self):
        pass
    def delete(self,booking_id=0):
        futsal_name=request.json['futsal_name']
        email=request.json['email']
        phone=request.json['phone']
        booking_data=request.json['booking_data']
        booking_time=request.json['booking_time']
        checking_data=request.json['checking_data']
        checking_time=request.json['checking_time']
        cur3 = dbconnection.cursor()
        cur3.execute("DELETE FROM  booking WHERE booking_id=%s",(futsal_name,email,phone,booking_data,booking_time,checking_data,checking_time,booking_id))
        dat2 = cur3.fetchone()
        if dat2:
            return json.dumps({'msg':'delete Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Already delete','status_code':'400'})
        cur.close()

     
