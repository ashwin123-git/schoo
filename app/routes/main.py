from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    # Note: JWT protection happens on the API endpoints, not on the page itself
    # The client-side JavaScript will validate the token for API calls
    return render_template('dashboard.html')

@main_bp.route('/health')
def health():
    return {'status': 'healthy'}, 200
