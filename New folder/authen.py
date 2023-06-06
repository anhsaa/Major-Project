# from flask import request
# from flask_restx import Namespace, Resource
# from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)

# auth_ns = Namespace('auth', description='Authentication and Authorization')
# jwt = JWTManager()
# jwt_config = {
#     'JWT_SECRET_KEY': 'your-secret-key',  # Change this to a secure secret key
#     'JWT_ACCESS_TOKEN_EXPIRES': 3600  # Access token expiration time in seconds
# }
# def configure_jwt(app):
#     jwt.init_app(app)

# @auth_ns.route('/login')
# class UserLogin(Resource):
#     @auth_ns.expect(todo)
#     def post(self):
        
#         username = request.json.get('username')
#         password = request.json.get('password')
    
#         if username == 'admin' and password == 'adminpassword':
#             access_token = create_access_token(identity=username)
#             return {'access_token': access_token}
#         else:
#             return {'message': 'Invalid credentials'}

# @auth_ns.route('/protected')
# class ProtectedResource(Resource):
#     @jwt_required
#     def get(self):
#         # Access token verification passed, user is authenticated
#         current_user = get_jwt_identity()
#         return {'message': f'Protected resource accessed by user: {current_user}'}