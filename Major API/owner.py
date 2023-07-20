from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from flask_cors import cross_origin
from flask import request,jsonify
import json
from authen import token_required
from dbConnection import conn
from Config import api


own=api.model('Own', {
    'owner_name': fields.String(required=True, description='The task details'),
    'password':fields.String(),
    'email': fields.String(required=True, description='The task details'),
    'contact': fields.String(required=True, description='The task details')
    })

name_space=api.namespace('Owner','all about user register')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','DELETE'])
@name_space.route('/CRUD/<int:owner_id>',methods=['GET','PUT'])
class ownerCRUD(Resource):
    @api.expect(own)
    @token_required
    @api.doc(params={'owner_name': 'As String','password':'As string','email':'As string','conatct':'As String'})
    
    def post(self):
        dbconn=conn()
        cur1 = dbconn.cursor()
        try:
            owner_name=request.json['owner_name']
            password=request.json['password']
            email=request.json['email']
            contact=request.json['contact']
            cur1.execute("INSERT INTO owner(owner_name, password, email, contact) values(%s,%s,%s,%s)",(owner_name, password,email,contact,))
            dbconn.commit()
            new_user_id = cur1.lastrowid
            if new_user_id:
                return jsonify({'msg': 'Successfully', 'status_code': 200})
            else:
                return jsonify({'msg': 'Already exist', 'status_code': 200})
        except Exception as ex1:
            raise ex1
        finally:
            cur1.close()
            dbconn.close()

    @api.expect(own)
    @api.doc(params={'owner_name': 'As String','password':'As string','email':'As string','conatct':'As String'})
    def put(self,owner_id=0):
        dbconn=conn()
        cur2 = dbconn.cursor()
        try:
            owner_name=request.json['owner_name']
            password=request.json['password']
            email=request.json['email']
            contact=request.json['contact']
            cur2 = dbconn.cursor()
            cur2.execute("UPDATE owner SET owner_name=%s,password=%s, email=%s,contact=%s WHERE owner_id=%s ",(owner_name,email,contact,password,owner_id,))
            # dat2 = cur3.fetchone()
            dbconn.commit()
            return json.dumps({'msg': 'Update successful', 'status_code': 200})
        except Exception as ex:
            raise ex

        
    def get(self):
        dbconn=conn()
        cur9 = dbconn.cursor()
        cur9.execute("SELECT * FROM owner")
        dat9 = cur9.fetchall() 
        dbconn.commit()
        return dat9
        



        

    # def get(self, owner_id):

    #     cur = dbconnection.cursor()
    #     cur.execute("SELECT * FROM owner WHERE owner_id = %s", (owner_id,))
    #     data = cur.fetchall()
    #     dbconnection.close()
    #     return data
    

   
            
        









