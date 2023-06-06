from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api


venue=api.model('Venue', {
    'venue_name': fields.String(required=True, description='The task details'),
    'email': fields.String(required=True, description='The task details'),
    'location': fields.String(required=True, description='The task details'),
    'contact': fields.String(required=True, description='The task details'),
    'image': fields.String(required=True, description='The task details'),
    'price': fields.String(required=True,description='The task details'),
    'rating': fields.String(required=True, description='The task details'),
    'description': fields.String(required=True, description='The task details')

    })

name_space=api.namespace('Venue','All about Fustal Detail ')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:venue_id>',methods=['POST'])
class venueCRUD(Resource):
    @api.expect(venue)
    @api.doc(params={'venue_name': 'As String','email':'As string','location':'As string',
                     'contact':'As string','image':'As string','rating':'As integer',
                     'description':'As string'})
    
    def post(self):
        venue_name=request.json['venue_name']
        email=request.json['email']
        location=request.json['location']
        contact=request.json['contact']
        image=request.json['image']
        rating=request.json['rating']
        description=request.json['description']
        cur6 = dbconnection.cursor()
        cur6.execute("INSERT INTO venue(venue_name,email,location,contact,image,rating,description) values(%s,%s,%s,%s,%s,%s,%s)",((venue_name,email,location,contact,image,rating,description,)))
        dbconnection.commit()
        if cur6.rowcount > 0:
            return json.dumps({'msg':'Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Already','status_code':'400'})



    def put(self,venue_id=0):
        try:
            data = request.get_json()
            if data is None:
                return {'msg': 'No JSON data provided', 'status_code': 400}

            if 'venue_name' not in data or 'email' not in data or 'location' not in data or 'contact' not in data or 'image' not in data or 'rating' not in data or 'description' not in data:
                return {'msg': 'Missing required fields', 'status_code': 400}
            
            venue_name=request.json['venue_name']
            email=request.json['email']
            location=request.json['location']
            contact=request.json['contact']
            image=request.json['image']
            rating=request.json['rating']
            description=request.json['description']
            cur = dbconnection.cursor()
            cur.execute("UPDATE venue SET venue_name=%s, email=%s, location=%s, contact=%s, image=%s, rating=%s, description=%s WHERE venue_id=%s",
                (venue_name, email, location, contact, image, rating, description, venue_id,))
            dbconnection.commit()

            if cur.rowcount > 0:
                return {'msg': 'Update successful', 'status_code': 200}
            else:
                return {'msg': 'No rows updated', 'status_code': 400}
        except Exception as e:
            return {'msg': 'Error occurred: ' + str(e), 'status_code': 500}


    def delete(self, venue_id):
        cur4 = dbconnection.cursor()
        cur4.execute("UPDATE venue SET delete_flag = 0 WHERE booking_id = {venue_id}")
        dbconnection.commit()
        dbconnection.delete(venue_id)
        if cur.rowcount > 0:
            return {'msg': 'Delete successful', 'status_code': 200}
        else:
            return {'msg': 'Already deleted', 'status_code': 400}


    def get(self, venue_id=None):
        if venue_id is not None:
            cur = dbconnection.cursor()
            cur.execute("SELECT * FROM venue WHERE venue_id = %s", (venue_id,))
            data = cur.fetchone()
            dbconnection.commit()
            if data:
                return {'msg': data, 'status_code': '200'}
            else:
                return {'msg': 'No data found', 'status_code': '404'}
        else:
            cur = dbconnection.cursor()
            cur.execute("SELECT * FROM venue")
            data = cur.fetchall()
            dbconnection.commit()
            if data:
                return {'msg': data, 'status_code': '200'}
            else:
                return {'msg': 'No data found', 'status_code': '404'}
            


    
     
