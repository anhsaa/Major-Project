import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api
import os
from authen import token_required


img_model = api.model('Image', {
    'image': fields.String(required=True, description='The task details')
})

name_space = api.namespace('Image', 'Display the image')


@name_space.route("/CRUD", methods=['GET'])
@name_space.route('/CRUD/<int:id>', methods=['POST','DELETE','PUT'])
class UploadImage(Resource):
    @api.expect(img_model)
    @token_required
    @api.doc(params={'image': 'As String'})

    def post(self):
        cur = dbconnection.cursor()
        try:
            image = request.files['image']
            if "img" in request.files:
                image = request.files['img']
                image.save(r"D:\API\Upload\futsal1.jpg")
                return json.dumps({"message": "Image uploaded successfully"})
            else:
                return json.dumps({"message": "Invalid image"})
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            dbconnection.close()

    @token_required
    def get(self):
        cur2 = dbconnection.cursor()
        try:
            return json.dumps({"message": "GET method called"})
        except Exception as ex:
            raise ex
        finally:
            cur2.close()
            dbconnection.close()

    @token_required
    def put(self):
        cur3 = dbconnection.cursor()
        try:
            if 'image' in request.files:
                image = request.files['image']
                return json.dumps({"message": "Image updated successfully"})
            else:
                return json.dumps({"message": "Invalid image"})
        except Exception as ex:
            raise ex
        finally:
            cur3.close()
            dbconnection.close()

    @token_required
    def delete(self, id):
        cur4 = dbconnection.cursor()
        try:   
            return json.dumps({"message": "Image deleted successfully"})
        except Exception as ex:
            raise ex
        finally:
            cur4.close()
            dbconnection.close()


