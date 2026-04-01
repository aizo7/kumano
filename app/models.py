# データモデル（後で拡張）
from app import db

class Spot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # コンビニ, ホテル, 飲食店, etc.
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    photo_url = db.Column(db.String(200))
    open_time = db.Column(db.String(20))
    close_time = db.Column(db.String(20))
    recommended_menu = db.Column(db.String(200))
    reservation_url = db.Column(db.String(200))
    is_world_heritage = db.Column(db.Boolean, default=False)