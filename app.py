from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask import request
from dataclasses import dataclass

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pruebaCD'
    db.init_app(app)
    with app.app_context():
        import routes
        db.create_all()
        return app

