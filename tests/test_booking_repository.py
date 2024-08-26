from datetime import date
from lib.booking_repository import BookingRepository
from lib.booking import Booking

"""
When we call the all method we should get a list of all bookings
"""
def test_get_all(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = BookingRepository(db_connection)

    bookings = repository.all()

    assert bookings == [
        Booking(1, 1, 2, 1, date(2024, 5, 10), "approved"),
        Booking(2, 2, 3, 2, date(2024, 5, 15), "pending"),
        Booking(3, 3, 4, 3, date(2024, 5, 20), "denied"),
        Booking(4, 4, 1, 4, date(2024, 5, 25), "approved")
]

"""
When we call the find method
we get a single booking object reflecting the seed data
"""
def test_get_single_booking(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = BookingRepository(db_connection)

    booking = repository.find(3)
    assert booking == Booking(3, 3, 4, 3, date(2024, 5, 20), "denied")

"""
When we call the create method
we get a new record in the database
"""
def test_create_booking(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = BookingRepository(db_connection)

    created_booking = repository.create(Booking(None, 1, 2, 2, date(2024, 5, 30), "denied"))
    assert created_booking == Booking(5, 1, 2, 2, date(2024, 5, 30), "denied")

    bookings = repository.all()
    assert bookings == [
        Booking(1, 1, 2, 1, date(2024, 5, 10), "approved"),
        Booking(2, 2, 3, 2, date(2024, 5, 15), "pending"),
        Booking(3, 3, 4, 3, date(2024, 5, 20), "denied"),
        Booking(4, 4, 1, 4, date(2024, 5, 25), "approved"),
        Booking(5, 1, 2, 2, date(2024, 5, 30), "denied")
]

"""
When we call the delete method
the record should be removed from the database
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = BookingRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Booking(1, 1, 2, 1, date(2024, 5, 10), "approved"),
        Booking(2, 2, 3, 2, date(2024, 5, 15), "pending"),
        Booking(4, 4, 1, 4, date(2024, 5, 25), "approved"),
]
"""
When we call the delete method
the record should be removed from the database
"""
def test_find_by_guest_id(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = BookingRepository(db_connection)
    result = repository.find_by_guest_id(1)
    assert result == [Booking(4, 4, 1, 4, date(2024, 5, 25), "approved")]

def test_find_by_host_id(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = BookingRepository(db_connection)
    result = repository.find_by_host_id(1)
    assert result == [Booking(1, 1, 2, 1, date(2024, 5, 10), "approved")]
    