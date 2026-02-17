from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User, Log
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import io

logs_bp = Blueprint('logs', __name__, url_prefix='/api/logs')

@logs_bp.route('/add', methods=['POST'])
@jwt_required()
def add_log():
    """Add a new income or expense log"""
    current_user_id = int(get_jwt_identity())
    data = request.get_json()
    
    if not data or not data.get('amount') or not data.get('log_type'):
        return jsonify({'error': 'Amount and log_type required'}), 400
    
    if data['log_type'] not in ['income', 'expense']:
        return jsonify({'error': 'log_type must be income or expense'}), 400
    
    try:
        log = Log(
            user_id=current_user_id,
            log_type=data['log_type'],
            amount=float(data['amount']),
            description=data.get('description', '')
        )
        
        db.session.add(log)
        db.session.commit()
        
        return jsonify({
            'message': 'Log added successfully',
            'log': log.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@logs_bp.route('/list', methods=['GET'])
@jwt_required()
def list_logs():
    """Get all shared logs (from all businessmen) with optional filtering"""
    current_user_id = int(get_jwt_identity())
    
    # Get filter parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    log_type = request.args.get('log_type')
    
    # Get ALL logs (shared across all users), not just current user's
    query = Log.query
    
    # Apply filters
    if start_date:
        try:
            start = datetime.fromisoformat(start_date)
            query = query.filter(Log.created_at >= start)
        except:
            pass
    
    if end_date:
        try:
            end = datetime.fromisoformat(end_date)
            # Add one day to include the entire end date
            end = end + timedelta(days=1)
            query = query.filter(Log.created_at < end)
        except:
            pass
    
    if log_type and log_type in ['income', 'expense']:
        query = query.filter_by(log_type=log_type)
    
    logs = query.order_by(Log.created_at.desc()).all()
    
    # Calculate totals from ALL logs
    all_logs = Log.query.all()
    total_income = sum(log.amount for log in all_logs if log.log_type == 'income')
    total_expense = sum(log.amount for log in all_logs if log.log_type == 'expense')
    total_balance = total_income - total_expense
    
    # Convert logs to dict and add creator info
    logs_data = []
    for log in logs:
        log_dict = log.to_dict()
        # Add user info who created this log
        user = User.query.get(log.user_id)
        if user:
            log_dict['created_by'] = user.full_name or user.email
            log_dict['created_by_email'] = user.email
        logs_data.append(log_dict)
    
    return jsonify({
        'logs': logs_data,
        'totals': {
            'income': total_income,
            'expense': total_expense,
            'balance': total_balance
        }
    }), 200

@logs_bp.route('/summary', methods=['GET'])
@jwt_required()
def get_summary():
    """Get income, expense, and balance summary (all shared logs)"""
    current_user_id = int(get_jwt_identity())
    
    # Get ALL logs from all businessmen (shared)
    logs = Log.query.all()
    
    total_income = sum(log.amount for log in logs if log.log_type == 'income')
    total_expense = sum(log.amount for log in logs if log.log_type == 'expense')
    total_balance = total_income - total_expense
    
    return jsonify({
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance
    }), 200

@logs_bp.route('/export-pdf', methods=['GET'])
@jwt_required()
def export_pdf():
    """Export ALL shared logs as PDF with creator info"""
    current_user_id = int(get_jwt_identity())
    current_user = User.query.get(current_user_id)
    
    # Get filter parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Get ALL logs (shared), not just current user's
    query = Log.query
    
    if start_date:
        try:
            start = datetime.fromisoformat(start_date)
            query = query.filter(Log.created_at >= start)
        except:
            pass
    
    if end_date:
        try:
            end = datetime.fromisoformat(end_date)
            end = end + timedelta(days=1)
            query = query.filter(Log.created_at < end)
        except:
            pass
    
    logs = query.order_by(Log.created_at.desc()).all()
    
    # Create PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=30,
        alignment=1  # Center
    )
    
    # Title
    elements.append(Paragraph('Business Log Report (All Team Members)', title_style))
    elements.append(Paragraph(f'Exported by: {current_user.email}', styles['Normal']))
    elements.append(Paragraph(f'Generated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}', styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Calculate totals
    total_income = sum(log.amount for log in logs if log.log_type == 'income')
    total_expense = sum(log.amount for log in logs if log.log_type == 'expense')
    total_balance = total_income - total_expense
    
    # Summary
    summary_data = [
        ['Total Income', f'₹{total_income:.2f}'],
        ['Total Expense', f'₹{total_expense:.2f}'],
        ['Balance', f'₹{total_balance:.2f}']
    ]
    
    summary_table = Table(summary_data)
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10b981')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(summary_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Logs table
    table_data = [['Date', 'Type', 'Amount', 'Added By', 'Description']]
    
    for log in logs:
        user = User.query.get(log.user_id)
        creator_name = (user.full_name or user.email) if user else 'Unknown'
        table_data.append([
            log.created_at.strftime('%Y-%m-%d'),
            log.log_type.capitalize(),
            f'₹{log.amount:.2f}',
            creator_name,
            log.description[:30]
        ])
    
    if len(table_data) > 1:
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3b82f6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f3f4f6')])
        ]))
        elements.append(table)
    else:
        elements.append(Paragraph('No logs found', styles['Normal']))
    
    doc.build(elements)
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'business_logs_{datetime.utcnow().strftime("%Y%m%d_%H%M%S")}.pdf'
    )

@logs_bp.route('/delete/<int:log_id>', methods=['DELETE'])
@jwt_required()
def delete_log(log_id):
    """Delete a log"""
    current_user_id = int(get_jwt_identity())
    
    log = Log.query.get(log_id)
    if not log:
        return jsonify({'error': 'Log not found'}), 404
    
    if log.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    try:
        db.session.delete(log)
        db.session.commit()
        return jsonify({'message': 'Log deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
