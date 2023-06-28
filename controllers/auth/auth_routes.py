from functools import wraps
from flask import Blueprint, jsonify, request
from repositories.user_repository import UserRepository
from auth.auth import AuthManager

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    auth_result = AuthManager.authenticate(email, password)

    if auth_result:
        return jsonify(auth_result), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({'error': 'Authentication token not provided'}), 401

    result = AuthManager.logout(token)
    return jsonify(result)

        