from flask import Flask, render_template
from flask_restx import Resource, Api, fields
from flask_cors import cross_origin
from flask import request, jsonify
import json
from Config import api, dbconnection


todo = api.model('Todo', {
    'email': fields.String(required=True, description='The task details'),
    'password': fields.String()
})
name_space = api.namespace('User', 'all about users')


@cross_origin
@name_space.route("/CRUD", methods=['GET', 'POST', 'PUT', 'DELETE'])
@name_space.route('/CRUD/<int:id>', methods=['GET'])
class userCRUD(Resource):
    @api.expect(todo)
    @api.doc(params={'email': 'As String', 'password': 'As string'})
    def post(self):
        email = request.json['email']
        password = request.json['password']
        cur = dbconnection.cursor()
        cur.execute(
            "SELECT * FROM user WHERE email = %s AND password = %s", (email, password,))
        dat = cur.fetchone()
        if dat:
            return jsonify({'msg': 'Registered Successfully', 'status_code': '200'})
        else:
            return jsonify({'msg': 'Login Failed', 'status_code': '400'})
        cur.close()  # closing a cursor

    def get(self):
        pass


reg = api.model('Reg', {
    'username': fields.String(required=True, description='The task details'),
    'password': fields.String(),
    'email': fields.String(required=True, description='The task details'),
    'contact': fields.String(required=True, description='The task details')
})

name_space = api.namespace('Register', 'all about user register')


@cross_origin
@name_space.route("/CRUD", methods=['GET', 'POST', 'PUT', 'DELETE'])
@name_space.route('/CRUD/<int:id>', methods=['GET'])
class registerCRUD(Resource):
    @api.expect(reg)
    @api.doc(params={'username': 'As String', 'password': 'As string', 'email': 'As string', 'phone': 'As String'})
    def post(self):
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        contact = request.json['contact']
        cur1 = dbconnection.cursor()
        cur1.execute("INSERT INTO user(username, password, email, contact) values(%s,%s,%s,%s)",
                     (username, password, email, contact,))
        # dat = cur1.fetchone()
        dbconnection.commit()
        new_user_id = cur1.lastrowid
        if new_user_id:
            return jsonify({'msg': 'Registered Successfully', 'status_code': '200'})
        else:
            return jsonify({'msg': 'Already exist', 'status_code': '200'})

        cur.close()  # closing a cursor

    def get(self):
        pass
