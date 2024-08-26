from lib.booking import Booking

"""
I want to see if Booking is correctly intialised
It should have the id, host_id, guest_id, space_id, booking_date, current_booking_status.
"""
def test_booking_constructs():
    booking = Booking(1, 1, 2, 1, '2024-05-10', 'approved')
    assert booking.id == 1
    assert booking.host_id == 1
    assert booking.guest_id == 2
    assert booking.space_id == 1
    assert booking.booking_date == '2024-05-10'
    assert booking.booking_status == 'approved'

"""
We want to see if the booking is formatted nicely
"""
def test_formated_nicely():
    booking = Booking(1, 1, 2, 1, '2024-05-10', 'approved')
    assert str(booking) == "Booking(1, 1, 2, 1, 2024-05-10, approved)"

"""
We want to see if two identical bookings are the same
"""
def test_equal_bookings():
    booking1 = Booking(1, 1, 2, 1, '2024-05-10', 'approved')
    booking2 = Booking(1, 1, 2, 1, '2024-05-10', 'approved')
    assert booking1 == booking2