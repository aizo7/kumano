# 設定ファイル（APIキーなど）
GOOGLE_MAPS_API_KEY = 'AIzaSyCIkONpQ1_TxGDSiLtxotQ4FXR-JI-2ROs'  # Google Maps APIキーをここに設定

# データベース設定
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'instance', 'spots.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False