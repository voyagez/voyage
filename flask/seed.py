from random import choice as rc, randrange

from app import app
from models import db, Hotel, Room

if __name__ == "__main__":
    with app.app_context():
        print("Clearing db...")
        Hotel.query.delete()
        Room.query.delete()

        print("Seeding hotels...")
        hotels = [
            Hotel(name="Insomnia Cookies",
                hotel_type="Resort",
                city="NYC",
                address="11 Broadway",
                distance=0,
                photo="",
                title="Flatiron",
                desc="Flatiron",
                rating=4,
                num_of_rooms="2",
                cheapest_price=100,
                featured=False,
            ),
            Hotel(
                name="Insomnia Cookies",
                hotel_type="Cabin",
                city="Brooklyn",
                address="10 Havemeyer",
                distance=0,
                photo="",
                title="Kill me",
                desc="aaah",
                rating=3,
                num_of_rooms="3",
                cheapest_price=200,
                featured=False,
            ),
            Hotel(
                name="Insomnia Cookies",
                hotel_type="Resort",
                city="Philadelphia",
                address="10 Bond",
                distance=0,
                photo="",
                title="Wow Best Hotel",
                desc="amazing!",
                rating=5,
                num_of_rooms="3",
                cheapest_price=500,
                featured=False,
            ),
            Hotel(
                name="Insomnia Cookies",
                hotel_type="Resort",
                city="NYC",
                address="201 Grand",
                distance=4,
                photo="",
                title="Another Hotel!",
                desc="anotha one",
                rating=2,
                num_of_rooms="2",
                cheapest_price=20,
                featured=False,
            ),
            Hotel(
                name="Insomnia Cookies",
                hotel_type="Resort",
                city="NYC",
                address="150 E Broadway",
                distance=3,
                photo="",
                title="wow its amazing",
                desc="wow so cool",
                rating=4,
                num_of_rooms="2",
                cheapest_price=20,
                featured=False,
            ),
        ]

        db.session.add_all(hotels)
        db.session.commit()

        print("Seeding rooms...")
        rooms = [
            Room(
                title="Suite",
                price=400,
                max_people=2,
                desc="Wow so nice",
                room_numbers=202,
                hotel_id=1
            ),
            Room(
                title="The Shining",
                price=666,
                max_people=1,
                desc="A lovely lady stays here",
                room_numbers=237,
                hotel_id=1
            ),
            Room(
                title="Johnson",
                price=200,
                max_people=100,
                desc="spacious",
                room_numbers=10,
                hotel_id=2
            ),
            Room(
                title="Double suite",
                price=20,
                max_people=2,
                desc="romantic",
                room_numbers=123,
                hotel_id=1
            ),
            Room(
                title="Cabana",
                price=300,
                max_people=3,
                desc="luxurious",
                room_numbers=4,
                hotel_id=2
            ),
            Room(
                title="Suite",
                price=450,
                max_people=1,
                desc="good",
                room_numbers=10,
                hotel_id=1
            ),
            Room(
                title="Another Suite",
                price=300,
                max_people=3,
                desc="great",
                room_numbers=9,
                hotel_id=2
            ),
        ]

        db.session.add_all(rooms)

        db.session.commit()

        print("Done seeding!")
