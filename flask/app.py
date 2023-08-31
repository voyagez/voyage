from models import db, Hotel, Room
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/hotels')
def get_hotels():
    hotels = Hotel.query.all()
    data = [hotel.to_dict() for hotel in hotels]
    return make_response(jsonify(data), 200)

@app.post('/hotels')
def post_hotels():
    try:
        json_data = request.get_json()
        hotel = Hotel(price = json_data['price'])
        db.session.add(hotel)
        db.session.commit()
        return make_response(jsonify(hotel.to_dict()), 201)
    except:
        return make_response(jsonify({ "errors": ["validation errors"] }), 405)

@app.get('/rooms')
def get_rooms():
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)
