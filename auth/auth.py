import jwt
from flask import request, jsonify
from functools import wraps
from repositories.user_repository import UserRepository
from config import JWT_SECRET_KEY, BLOCK_LIST_TOKEN
import time


class AuthManager():

    def generate_access_token(email, user_id, tipo):
        payload = {'email': email,
                   'id': user_id,
                   'tipo': tipo,
                   'exp': time.time() + 86400}
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
        return token

    def authenticate(email, senha):
        user = UserRepository.get_user_by_email(email)

        if user and senha == user.senha:
            token = AuthManager.generate_access_token(email, user.id, user.tipo)
            return {'token': token, 'tipo': user.tipo}

        return None 

    def verify_token(token):
        try:
            decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            if token in BLOCK_LIST_TOKEN or decoded_token['exp'] < time.time():
                return False
            return True
        except jwt.InvalidTokenError:
            return False

    def logout(token):
        try:
            token = str.replace(str(token), 'Bearer ', '')
            # decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            # jti = decoded_token['jti']
            BLOCK_LIST_TOKEN.add(token)
            return {'message': 'Successful logout'},200
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}, 401


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers['Authorization']
        token = str.replace(str(token), 'Bearer ', '')
        if token:
            is_valid = AuthManager.verify_token(token)
            if is_valid:
                return func(*args, **kwargs)

        return jsonify({'error': 'Access denied'}), 401

    return wrapper

