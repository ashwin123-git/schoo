from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User, Message
from datetime import datetime

chat_bp = Blueprint('chat', __name__, url_prefix='/api/chat')

@chat_bp.route('/send', methods=['POST'])
@jwt_required()
def send_message():
    """Send a message to group chat"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    if not data or not data.get('content'):
        return jsonify({'error': 'Content required'}), 400
    
    if not data['content'].strip():
        return jsonify({'error': 'Content cannot be empty'}), 400
    
    try:
        message = Message(
            user_id=current_user_id,
            content=data['content'].strip()
        )
        
        db.session.add(message)
        db.session.commit()
        
        return jsonify({
            'message': 'Message sent successfully',
            'data': message.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/messages', methods=['GET'])
@jwt_required()
def get_messages():
    """Get all group chat messages"""
    current_user_id = int(get_jwt_identity())
    
    # Get limit and offset from query params
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    # Get total count
    total = Message.query.count()
    
    # Get messages
    messages = Message.query.order_by(Message.created_at.desc()).limit(limit).offset(offset).all()
    
    return jsonify({
        'messages': [msg.to_dict() for msg in reversed(messages)],  # Reverse to show oldest first
        'total': total,
        'limit': limit,
        'offset': offset
    }), 200

@chat_bp.route('/delete/<int:message_id>', methods=['DELETE'])
@jwt_required()
def delete_message(message_id):
    """Delete a message (only by sender or admin)"""
    current_user_id = int(get_jwt_identity())
    
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    if message.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    try:
        db.session.delete(message)
        db.session.commit()
        return jsonify({'message': 'Message deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/edit/<int:message_id>', methods=['PUT'])
@jwt_required()
def edit_message(message_id):
    """Edit a message (only by sender)"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    if not data or not data.get('content'):
        return jsonify({'error': 'Content required'}), 400
    
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    if message.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    try:
        message.content = data['content'].strip()
        db.session.commit()
        return jsonify({
            'message': 'Message edited successfully',
            'data': message.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
