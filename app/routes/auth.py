from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
from app import db
from app.models import User
from datetime import datetime
import string
import random

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Store verification codes temporarily
verification_codes = {}

def generate_verification_code():
    """Generate a 6-digit verification code"""
    return ''.join(random.choices(string.digits, k=6))

@auth_bp.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@auth_bp.route('/signin', methods=['GET'])
def signin_page():
    return render_template('signin.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400
    
    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    # Create new user
    user = User(
        email=data['email'],
        full_name=data.get('full_name', ''),
        is_verified=False
    )
    user.set_password(data['password'])
    
    try:
        db.session.add(user)
        db.session.commit()
        
        # Generate verification code and display in console
        verification_code = generate_verification_code()
        verification_codes[data['email']] = verification_code
        
        # Display code in console for manual sending
        print(f"\n{'='*60}")
        print(f"📧 NEW USER REGISTRATION")
        print(f"{'='*60}")
        print(f"Email: {data['email']}")
        print(f"Verification Code: {verification_code}")
        print(f"{'='*60}\n")
        
        return jsonify({
            'message': 'User registered successfully. Check console for verification code.',
            'user_id': user.id,
            'email': user.email
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/verify-email', methods=['POST'])
def verify_email():
    """Verify email with code"""
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('code'):
        return jsonify({'error': 'Email and verification code required'}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Verify the code
    stored_code = verification_codes.get(data['email'])
    if not stored_code or stored_code != data['code']:
        return jsonify({'error': 'Invalid verification code'}), 400
    
    # Mark user as verified
    user.is_verified = True
    db.session.commit()
    
    # Remove the code after verification
    if data['email'] in verification_codes:
        del verification_codes[data['email']]
    
    return jsonify({'message': 'Email verified successfully'}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid email or password'}), 401
    
    if not user.is_verified:
        return jsonify({'error': 'Please verify your email first'}), 403
    
    # Create access token (convert user.id to string)
    access_token = create_access_token(identity=str(user.id))
    
    return jsonify({
        'message': 'Login successful',
        'access_token': access_token,
        'user': user.to_dict()
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Logout user"""
    return jsonify({'message': 'Logout successful'}), 200
