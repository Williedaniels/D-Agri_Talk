from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.knowledge import KnowledgeEntry

knowledge_bp = Blueprint('knowledge', __name__)

@knowledge_bp.route('/', methods=['GET'])
def get_knowledge_entries():
    entries = KnowledgeEntry.query.all()
    return jsonify([entry.to_dict() for entry in entries]), 200

@knowledge_bp.route('/', methods=['POST'])
@jwt_required()
def create_knowledge_entry():
    data = request.get_json()
    user_id = get_jwt_identity()
    
    entry = KnowledgeEntry(
        title=data['title'],
        content=data['content'],
        language=data.get('language', 'English'),
        crop_type=data.get('crop_type', ''),
        season=data.get('season', ''),
        region=data.get('region', ''),
        author_id=user_id
    )
    
    db.session.add(entry)
    db.session.commit()
    db.session.refresh(new_entry)
    
    return jsonify(new_entry.to_dict()), 201

@knowledge_bp.route('/<int:entry_id>', methods=['GET'])
def get_knowledge_entry(entry_id):
    entry = KnowledgeEntry.query.get_or_404(entry_id)
    return jsonify(entry.to_dict()), 200