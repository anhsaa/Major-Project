import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api

rate=api.model('Rate',{
    'venue_id':fields.String(required=True,description='venue'),
    'booking_id': fields.Integer(required=True, description='ID of the booking'),
    'rating': fields.Integer(required=True, description='Rating value (1-5)'),
})


name_space=api.namespace('Rating','all about rating fustsal')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:id>',methods=['POST'])
class rateCRUD(Resource):
    @api.expect(rate)
    @api.doc(params={'venue_id': 'As integer', 'rating':'As integer', 'booking_id':'As integer'})

    def post(self):
        venue_id=request.json['venue_id']
        booking_id=request.json['booking_id']
        rating=request.json['rating']
        cur = dbconnection.cursor()
        cur.execute("INSERT INTO rating (venue_id, booking_id, rating) VALUES (%s, %s, %s)", (venue_id, booking_id, rating))
        dat1 = cur.fetchone()
        if dat1:
            return json.dumps({'msg':'rate Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Already','status_code':'400'})

    def get(self):
        cur1=dbconnection.cursor()
        cur1.execute("SELECT * FROM rating")
        dat = cur1.fetchone()
        return dat
        

name_space=api.namespace('Average','all about averege rating of fustsal')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:id>',methods=['GET'])
class avgCRUD(Resource): 
    
    def get(self, id):
        venue_ratings = [rating['rating'] for rating in ratings if rating['venue_id'] == id]

        if not venue_ratings:
            return jsonify({'error': 'No ratings found for the specified venue'})

        average_rating = sum(venue_ratings) / len(venue_ratings)
        return jsonify({'average_rating': average_rating})
            




