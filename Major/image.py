import datetime
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask import request,jsonify
from flask_cors import cross_origin
import json
from Config import dbconnection,api
import os

name_space=api.namespace('Image','Display the image')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:id>',methods=['POST'])
class UploadImage(Resource):
    def post(self):
        if "img" in request.files:
            image = request.files["img"]
            image_name= 'futsal1.jpg'
            image.save("D:\API\Upload\futsal1.jpg",image_name)
            return json.dumps({"message": "Image uploaded successfully"})
        else:
            return json.dumps({"message": "Invalid image"})





