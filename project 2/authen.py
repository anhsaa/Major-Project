import json
from flask import request, jsonify
from flask import Flask, render_template
from flask_restx import Resource,Api,fields
from functools import wraps
from Config import api,dbconnection
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            id = checkToken(token)
            if len(id) > 0:
                sessiontype = checkTokenTime(token)
                if sessiontype:
                    return f(*args, **kwargs)
                else:
                    return json.dumps({'msg': 'Token expired', 'status_code': 401})
            else:
                return json.dumps({'msg': 'Unauthorized access', 'status_code': 401})
        if not token:
            return json.dumps({'msg': 'Invalid token', 'status_code': 401})
    return decorated


def checkTokenTime(token):
    try:
        decoded = jwt.decode(token, "ashnakey", algorithms="HS256")
        return True
    except jwt.ExpiredSignatureError:
        return False


def checkToken(token):
    cur = dbconnection.cursor()
    try:
        cur.execute("SELECT * FROM user WHERE token = %s",(token,))
        data = cur.fetchall()
        cur.close()
        dbconnection.close()

        if len(data) > 0:
            return data
        else:
            return []
    except Exception as ex:
        print(json.dumps({'msg': str(ex), 'status_code': 404}))
        return json.dumps({'msg': 'Error occurred', 'status_code': 500})


