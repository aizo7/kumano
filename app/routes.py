from app import app, db
from flask import render_template, jsonify
from app.models import Spot
import config

@app.route('/')
def home():
    return render_template('index.html', api_key=config.GOOGLE_MAPS_API_KEY)

@app.route('/api/spots')
def get_spots():
    spots = Spot.query.all()
    return jsonify([{
        'id': spot.id,
        'name': spot.name,
        'category': spot.category,
        'lat': spot.lat,
        'lng': spot.lng,
        'description': spot.description,
        'photo_url': spot.photo_url,
        'open_time': spot.open_time,
        'close_time': spot.close_time,
        'recommended_menu': spot.recommended_menu,
        'reservation_url': spot.reservation_url,
        'is_world_heritage': spot.is_world_heritage
    } for spot in spots])