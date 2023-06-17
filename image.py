import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api
import os


img_model = api.model('Image', {
    'image': fields.String(required=True, description='The task details')
})

name_space = api.namespace('Image', 'Display the image')


@name_space.route("/CRUD", methods=['GET', 'POST', 'PUT', 'DELETE'])
@name_space.route('/CRUD/<int:id>', methods=['POST'])
class UploadImage(Resource):
    @api.expect(img_model)
    @api.doc(params={'image': 'As String'})
    def post(self):
        try:
            image = request.json['image']
            if "img" in request.files:
                image = request.files['img']
                image.save(r"D:\API\Upload\futsal1.jpg")
                return json.dumps({"message": "Image uploaded successfully"})
            else:
                return json.dumps({"message": "Invalid image"})
        except Exception as ex:
            raise ex

        
        finally:
            dbconnection.close()





