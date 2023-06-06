from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask_cors import cross_origin
from flask import request,jsonify
import json
from Config import api,dbconnection


own=api.model('Own', {
    'owner_name': fields.String(required=True, description='The task details'),
    'password':fields.String(),
    'email': fields.String(required=True, description='The task details'),
    'contact': fields.String(required=True, description='The task details')
    })

name_space=api.namespace('Owner','all about user register')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:owner_id>',methods=['GET'])
class ownerCRUD(Resource):
    @api.expect(own)
    @api.doc(params={'owner_name': 'As String','password':'As string','email':'As string','conatct':'As String'})
    
    def post(self):
        owner_name=request.json['owner_name']
        password=request.json['password']
        email=request.json['email']
        contact=request.json['contact']
        cur1 = dbconnection.cursor()
        cur1.execute("INSERT INTO owner(owner_name, password, email, contact) values(%s,%s,%s,%s)",(owner_name, password,email,contact,))
        # dat = cur1.fetchone()
        dbconnection.commit()
        new_user_id = cur1.lastrowid
        if new_user_id:
            return jsonify({'msg': 'Successfully', 'status_code': 200})
        else:
            return jsonify({'msg': 'Already exist', 'status_code': 200})
        


    def put(self,owner_id=0):
        owner_name=request.json['owner_name']
        password=request.json['password']
        email=request.json['email']
        contact=request.json['contact']
        cur2 = dbconnection.cursor()
        cur2.execute("UPDATE owner SET owner_name=%s,password=%s, email=%s,contact=%s WHERE owner_id=%s ",(owner_name,email,contact,password,owner_id,))
        # dat2 = cur3.fetchone()
        dbconnection.commit()
        if cur2.rowcount > 0:
            return json.dumps({'msg': 'Update successful', 'status_code': 200})
        else:
            return json.dumps({'msg': 'No rows updated', 'status_code': 400})

        
    def get(self):
        cur9 = dbconnection.cursor()
        cur9.execute("SELECT * FROM owner")
        dat9 = cur9.fetchall() 
        dbconnection.commit()
        return dat9
        



        

    # def get(self, owner_id):

    #     cur = dbconnection.cursor()
    #     cur.execute("SELECT * FROM owner WHERE owner_id = %s", (owner_id,))
    #     data = cur.fetchall()
    #     dbconnection.close()
    #     return data
    

   
            
        









