from flask_restx import Resource,Api,fields
from flask_cors import cross_origin
from flask import request,jsonify
import json
from Config import api
from dbConnection import conn
import jwt
import datetime 
from authen import token_required

todo=api.model('Todo', {
    'user_name': fields.String(required=True, description='The task details'),
    'password':fields.String()
    })
    
name_space=api.namespace('User','all about users')
@cross_origin()
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:user_id>',methods=['GET'])
class userCRUD(Resource):
    @api.expect(todo)
    @api.doc(params={'user_name': 'As String','password':'As string'})

    def post(self):
        dbcon=conn()
        cur = dbcon.cursor()
        try:
            user_name=request.json['user_name']
            password=request.json['password']
            cur.execute("SELECT user_id FROM user WHERE user_name = %s AND password = %s", (user_name, password,))
            dat = cur.fetchone()
            print(dat)
            if dat:
              
    
                token = jwt.encode({'user_name': user_name, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=240)}, "ashnaSkey",algorithm="HS256")
                cur = dbcon.cursor()
                cur.execute("UPDATE user SET token = %s WHERE user_id = %s", (token, dat[0],))
                dbcon.commit()
                cur.close()
                return jsonify({'msg':token,'status_code':'200'})
            else:
                return jsonify({'msg':'Login Failed','status_code':'400'})
        except Exception as ex1:
            raise ex1
        finally:
            cur.close()
            dbcon.close()
                

    def get(self):
        dbcon=conn()
        cur=dbcon.cursor()
        try:
            cur.execute("SELECT * FROM user")
            date=cur.fetchall()
            return date
        except Exception as e1:
            raise e1 
        finally:
            cur.close()
            dbcon.close()

reg=api.model('Reg', {
    'user_name': fields.String(required=True, description='The task details'),
    'password':fields.String(),
    'email': fields.String(required=True, description='The task details'),
    'contact': fields.String(required=True, description='The task details')
    })

name_space=api.namespace('Register','all about user register')
@cross_origin
@name_space.route("/CRUD",methods=['GET','POST','PUT','DELETE'])
@name_space.route('/CRUD/<int:id>',methods=['GET'])
class registerCRUD(Resource):
    @api.expect(reg)
    @api.doc(params={'user_name': 'As String','password':'As string','email':'As string','contact':'As String'})
    
    def post(self):
        dbcon=conn()
        cur1= dbcon.cursor()
        try:
            user_name=request.json['user_name']
            password=request.json['password']
            email=request.json['email']
            contact=request.json['contact']
            cur1.execute("INSERT INTO user(user_name, password, email, contact) values(%s,%s,%s,%s)",(user_name, password,email,contact,))
            dbcon.commit()
            if cur1.rowcount > 0:
                return json.dumps({'msg': 'Successfully', 'status_code': '200'})
            else:
                return json.dumps({'msg': 'Already', 'status_code': '400'})
        except Exception as ex:
            raise ex
        finally:
            cur1.close() 
            dbcon.close()

       
    def get(self):
        dbcon=conn()
        cur = dbcon.cursor()
        try:
            cur.execute("SELECT * FROM user")
            date1=cur.fetchall()
            return date1    
        except Exception as e:
            raise e 
        finally:
            cur.close()
            dbcon.close()










