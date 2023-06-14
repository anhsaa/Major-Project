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
@name_space.route("/CRUD",methods=['GET'])
@name_space.route('/CRUD/<int:venue_id>',methods=['POST','PUT','DELETE'])
class venueCRUD(Resource):
    @api.expect(venue)
    @api.doc(params={'venue_name': 'As String','email':'As string','location':'As string',
                     'contact':'As string','image':'As string','rating':'As integer',
                     'description':'As string'})
    
    def post(self):
        cur6 = dbconnection.cursor()
        try:
            venue_name=request.json['venue_name']
            email=request.json['email']
            location=request.json['location']
            contact=request.json['contact']
            image=request.json['image']
            rating=request.json['rating']
            description=request.json['description'] 
            cur6.execute("INSERT INTO venue(venue_name,email,location,contact,image,rating,description) values(%s,%s,%s,%s,%s,%s,%s)",((venue_name,email,location,contact,image,rating,description,)))
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
    @api.doc(params={'venue_name': 'As String','email':'As string','location':'As string',
                     'contact':'As string','image':'As string','rating':'As integer',
                     'description':'As string'})
    
    def put(self,venue_id=0):
        cur = dbconnection.cursor()
        try:
            venue_name=request.json['venue_name']
            email=request.json['email']
            location=request.json['location']
            contact=request.json['contact']
            image=request.json['image']
            rating=request.json['rating']
            description=request.json['description']
            cur.execute("UPDATE venue SET venue_name=%s, email=%s, location=%s, contact=%s, image=%s, rating=%s, description=%s WHERE venue_id=%s",
                (venue_name, email, location, contact, image, rating, description, venue_id,))
            dbconnection.commit()
            return {'msg': 'Update successful', 'status_code': 200}
            
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()



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


    def get(self, venue_id=None):
        cur = dbconnection.cursor()
        try:
            if venue_id is not None:
                cur.execute("SELECT v.*, AVG(r.rating) AS average_rating FROM venue v LEFT JOIN rating r ON v.venue_id = r.venue_id WHERE v.venue_id = %s GROUP BY v.venue_id", (venue_id,))
                data = cur.fetchone()
                if data:
                    return {'msg': data, 'status_code': '200'}
                else:
                    return {'msg': 'No data found', 'status_code': '404'}
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()




    
     
