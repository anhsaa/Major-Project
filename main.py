from flask import Flask, render_template
from flask_restx import Api, Resource,fields
from flask import request,jsonify
import json
import mysql.connector

dbconnection=  connection = mysql.connector.connect(host='localhost',
                                         database='mydatabase',
                                         user='ashna',
                                         password='ashna')
app = Flask(__name__)


api = Api(app, version='1.0', title='Sample API',
    description='A sample API',
)

todo=api.model('Todo', {
    'username': fields.String(required=True, description='The task details'),
    'password':fields.String()
    })


@api.route('/my-resource', endpoint='my-resource',methods=["GET","POST"])
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    @api.marshal_with(todo)
    def get(self):
        return {"abc":"python","xyz":"class"}

    @api.doc(responses={403: 'Not Authorized'})
    @api.expect(todo)
    def post(self):
        username = request.json['username']
        password = request.json['password']
        cur = dbconnection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND paswword = %s", (username, password,))
        dat = cur.fetchone()
        if dat:
            return json.dumps({'msg':'Insert Successfully','status_code':'200'})
        else:
            return json.dumps({'msg':'Insert Failed','status_code':'400'})
        cur.close() # closing a cursor


@api.route('/register', endpoint='register',methods=["GET","POST"])
@api.doc(params={'id': 'An ID'})
class MyRegister(Resource):
    @api.marshal_with(todo)
    def get(self):
        return {"abc":"python","xyz":"class"}

    @api.doc(responses={403: 'Not Authorized'})
    @api.expect(todo)
    def post(self):
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        cur = dbconnection.cursor()
        cur.execute("INSERT INTO users(username, password, email)",(username, password,email,))
        dbconnection.commit()
        print(cur.lastrowid)
        # if dat: 
        #     return json.dumps({'msg':'Register Successfully','status_code':'200'})
        # else:
        #     return json.dumps({'msg':'Register Failed','status_code':'400'})
        # cur.close() # closing a cursor

if __name__ == '__main__':
    app.run(debug=True,port=6000)















# from flask import Flask, request, jsonify
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'

# # set up login manager
# login_manager = LoginManager()
# login_manager.init_app(app)

# # define user model
# class User(UserMixin):
#     def __init__(self, id):
#         self.id = id

# # set up user loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)

# # define login endpoint
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
    
#     # check if user exists and password is correct
#     if username == 'admin' and password == 'password':
#         user = User(1)
#         login_user(user)
#         return jsonify({'message': 'Logged in successfully'})
#     else:
#         return jsonify({'error': 'Invalid username or password'})

# # define logout endpoint
# @app.route('/logout', methods=['POST'])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({'message': 'Logged out successfully'})

# # define verification endpoint
# @app.route('/verify', methods=['POST'])
# @login_required
# def verify():
#     # check if verification code is correct
#     code = request.form['code']
#     if code == '1234':
#         return jsonify({'message': 'Verification successful'})
#     else:
#         return jsonify({'error': 'Invalid verification code'})

# if __name__ == '__main__':
#     app.run()


                                

# # app = Flask(__name__)
# # api = Api(app, version='1.0', title='Sample API',
# #     description='A sample API',
# # )

# # todo=api.model('Todo', {
# #     'username': fields.String(required=True, description='The task details'),
# #     'password':fields.String()
# #     })

# # @api.route('/my-resource', endpoint='my-resource',methods=["GET","POST"])
# # @api.doc(params={'id': 'An ID'})
# # class MyResource(Resource):
# #     @api.marshal_with(todo)
# #     def get(self):
# #         return {"username":"python","password":"class"}

# #     @api.doc(responses={403: 'Not Authorized'})
# #     @api.expect(todo)
# #     def post(self):
# #         username = request.json['username']
# #         password = request.json['password']
# #         cursor = dbconnection.cursor()
# #         cursor.execute("SELECT * FROM `users` WHERE username= %s AND password= %s"(username,password))
        
        
# #         return("every this complete")
     


#     # @api.route('/login', methods=['POST'])
#     # def login():
#     #     username = request.form['username']
#     #     password = request.form['password']
#     #     cur = dbconnection.cursor()
#     #     cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password,))
#     #     cur.close()

#     # @api.route('/logout')
#     # def logout():
#     #     session.clear()
#     #     return("executed")

#     # @api.route('/login', methods=['POST'])
#     # def login():
#     #     username = request.form['username']
#     #     password = request.form['password']
#     #     sql_select_Query = "select * from users"
#     #     cursor = dbconnection.cursor()
#     #     cursor.execute(sql_select_Query)
#     #     records = cursor.fetchall()
#     #     print(records)
#     #     return("complete")

# if __name__ == '__main__':
#     app.run(debug=True)

