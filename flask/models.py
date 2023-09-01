from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels'
    serialize_rules = ('-rooms.hotel',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hotel_type = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    distance = db.Column(db.Integer)
    photo = db.Column(db.String)
    title = db.Column(db.String)
    desc = db.Column(db.String)
    rating = db.Column(db.Integer)
    num_of_rooms = db.Column(db.String)
    cheapest_price = db.Column(db.Integer)
    featured = db.Column(db.Boolean, default=False)
    rooms = db.relationship('Room',
        back_populates='hotel',
        cascade='all, delete-orphan')
    def __repr__(self):
        return f'<Hotels {self.id}>'


class Room(db.Model, SerializerMixin):
    __tablename__ = 'rooms'
    serialize_rules = ('-hotel.rooms',)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    max_people = db.Column(db.Integer)
    desc = db.Column(db.String)
    room_numbers = db.Column(db.Integer)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    hotel = db.relationship('Hotel',
        back_populates='rooms')
    @validates('price')
    def validate_price_not_negative(self, key, price):
        if price < 0:
            raise ValueError('Price cannot be negative')
        return price
    def __repr__(self):
        return f'<Rooms {self.id}>'
