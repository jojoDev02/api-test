import jwt
from flask import request, jsonify
from functools import wraps
from repositories.user_repository import UserRepository
from config import JWT_SECRET_KEY
import time

block_list = set()

class AuthManager():

    def generate_access_token(email, user_id, user_type):
        payload = {'email': email,
                   'id': user_id,
                   'type': user_type,
                   'exp': time.time() + 86400}
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
        return token

    def authenticate(email, password):
        user = UserRepository.get_user_by_email(email)

        if user and password == user.password:
            token = AuthManager.generate_access_token(email, user.id, user.user_type)
            return {'token': token, 'user_type': user.user_type}

        return None 

    def verify_token(token):
        try:
            decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            if token in block_list or decoded_token['exp'] < time.time():
                return False
            return True
        except jwt.InvalidTokenError:
            return False

    def logout(token):
        
        try:
            token = str.replace(str(token), 'Bearer ', '')
            # decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            # jti = decoded_token['jti']
            block_list.add(token)
            print("---------------")
            print(block_list)
            return {'message': 'Logout bem-sucedido'},200
        except jwt.InvalidTokenError:
            return {'error': 'Token inválido'}, 401


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers['Authorization']
        token = str.replace(str(token), 'Bearer ', '')
        if token:
            is_valid = AuthManager.verify_token(token)
            if is_valid:
                return func(*args, **kwargs)

        return jsonify({'error': 'Acesso não autorizado'}), 401

    return wrapper

