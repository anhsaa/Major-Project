import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api

pay=api.model('Pay',{
    'payment_date':fields.Date(required=True,description='venue date (YYYY-MM-DD)'),
    'total_amt':fields.String(required=True, description='The task details'),
    'booking_id': fields.Integer(required=True, description='Booking ID')
    
})

name_space=api.namespace('Payment','Detail about payment')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:payment_id>',methods=['POST'])
class payCRUD(Resource):
    @api.expect(pay)
    @api.doc(params={'payment_date': 'As String','total_amt':'As string','booking_id': 'As Integer'}) 
    def post(self):
        cur = dbconnection.cursor()
        try:
            payment_date=request.json['payment_date']
            total_amt=request.json['total_amt']
            booking_id = request.json['booking_id']
            cur.execute("INSERT INTO payment(payment_date, total_amt, booking_id) VALUES (%s, %s, %s)",(payment_date, total_amt, booking_id,))
            dbconnection.commit()
            if cur.rowcount > 0:
                return json.dumps({'msg':'Successfully','status_code':'200'})
            else:
                return json.dumps({'msg':'failed','status_code':'200'})
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()
