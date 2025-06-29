from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.market import MarketListing
from datetime import datetime

market_bp = Blueprint('market', __name__)

@market_bp.route('/', methods=['GET'])
def get_market_listings():
    listings = MarketListing.query.filter_by(is_available=True).all()
    return jsonify([listing.to_dict() for listing in listings]), 200

@market_bp.route('/', methods=['POST'])
@jwt_required()
def create_market_listing():
    data = request.get_json()
    user_id = get_jwt_identity()
    
    listing = MarketListing(
        crop_name=data['crop_name'],
        quantity=data['quantity'],
        unit=data['unit'],
        price_per_unit=data['price_per_unit'],
        location=data['location'],
        description=data.get('description', ''),
        farmer_id=user_id
    )
    
    if data.get('harvest_date'):
        listing.harvest_date = datetime.strptime(data['harvest_date'], '%Y-%m-%d').date()
    
    if data.get('available_until'):
        listing.available_until = datetime.strptime(data['available_until'], '%Y-%m-%d').date()
    
    db.session.add(listing)
    db.session.commit()
    db.session.refresh(new_listing)
    
    return jsonify(new_listing.to_dict()), 201
