from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api
from authen import token_required


venue=api.model('Venue', {
    'venue_name': fields.String(required=True, description='The task details'),
    'owner_id': fields.Integer(required=True, description='Owner ID'),
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
@name_space.route("/CRUD",methods=['GET','POST'])
@name_space.route('/CRUD/<int:venue_id>',methods=['GET','PUT','DELETE'])
class venueCRUD(Resource):
    @api.expect(venue)
    @token_required
    @api.doc(params={'venue_name': 'As String','owner_id': 'As Integer','email':'As string','location':'As string',
                     'contact':'As string','image':'As string','rating':'As integer',
                     'description':'As string'})
    
    def post(self):
        cur6 = dbconnection.cursor()
        try:
            venue_name=request.json['venue_name']
            owner_id=request.json['owner_id']
            email=request.json['email']
            location=request.json['location']
            contact=request.json['contact']
            image=request.json['image']
            rating=request.json['rating']
            description=request.json['description'] 
            cur6.execute("INSERT INTO venue(venue_name,owner_id,email,location,contact,image,rating,description) values(%s,%s,%s,%s,%s,%s,%s,%s)",((venue_name,owner_id,email,location,contact,image,rating,description,)))
            dbconnection.commit()
            if cur6.rowcount > 0:
                return json.dumps({'msg':'Successfully','status_code':'200'})
            else:
                return json.dumps({'msg':'Already','status_code':'400'})
        except Exception as ex:
            raise ex
        finally:
            cur6.close()
            dbconnection.close()



    @api.expect(venue)
    @token_required
    @api.doc(params={'venue_name': 'As String','owner_id': 'As Integer','email':'As string','location':'As string',
                     'contact':'As string','image':'As string','rating':'As integer',
                     'description':'As string'})
    
    def put(self,venue_id=0):
        cur = dbconnection.cursor()
        try:
            venue_name=request.json['venue_name']
            owner_id=request.json['owner_id']
            email=request.json['email']
            location=request.json['location']
            contact=request.json['contact']
            image=request.json['image']
            rating=request.json['rating']
            description=request.json['description']
            cur.execute("UPDATE venue SET venue_name=%s, owner_id=%s, email=%s, location=%s, contact=%s, image=%s, rating=%s, description=%s WHERE venue_id=%s",
                (venue_name, owner_id, email, location, contact, image, rating, description, venue_id,))
            dbconnection.commit()
            return {'msg': 'Update successful', 'status_code': 200}
            
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()


    @token_required
    def delete(self, venue_id):
        cur= dbconnection.cursor()
        try: 
            cur.execute("UPDATE venue SET delete_flag = 1 WHERE booking_id = {venue_id}")
            dbconnection.commit()
            dbconnection.delete(venue_id)
            return {'msg': 'Delete successful', 'status_code': 200}

        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()

    @token_required
    def get(self, venue_id=-1):
        cur = dbconnection.cursor()
        try:
            if venue_id >0:
                cur.execute("SELECT v.*, AVG(r.rating) AS average_rating FROM venue v LEFT JOIN rating r ON v.venue_id = r.venue_id WHERE v.venue_id = %s GROUP BY v.venue_id", (venue_id,))
                data = cur.fetchone()
                if data:
                    return {'msg': data, 'status_code': 200}
                else:
                    return {'msg': 'No data found', 'status_code': 400}
            else:
                return {'msg': 'invalid id', 'status_code': 400}
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()
    
venuerating=api.model('VenueRating', {
    'venue_name': fields.String(required=True, description='The task details'),
    'rating': fields.Integer(required=True, description='Rating')
    })

@name_space.route('/venuRating',methods=['POST'])
class venueCRUD(Resource):
    @token_required
    @api.expect(venuerating)
    @api.doc(params={'venue_name': 'As String','rating': 'As Integer'})
    def post(self):
        cur = dbconnection.cursor()
        try:
            venue_id= request.json['venue_id']
            rating = request.json['rating']
            cur.execute("INSERT INTO venue(venue_id, rating) VALUES (%s, %s)", (venue_id, rating,))
            dbconnection.commit()
            return {'msg': 'Data posted successfully', 'status_code': '200'}
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()
    
     
