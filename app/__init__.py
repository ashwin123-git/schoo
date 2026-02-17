from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    
    # JWT error handlers
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return identity

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        return {}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({'error': 'Token has expired'}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'error': f'Invalid token: {error}'}), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'error': 'Missing Authorization Header'}), 401

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_data):
        return jsonify({'error': 'Token has been revoked'}), 401
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.logs import logs_bp
    from app.routes.chat import chat_bp
    from app.routes.main import main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(main_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
