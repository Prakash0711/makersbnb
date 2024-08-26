class Booking:
    def __init__(self, id, host_id, guest_id, space_id, booking_date, booking_status):
        self.id = id
        self.host_id = host_id
        self.guest_id = guest_id
        self.space_id = space_id
        self.booking_date = booking_date
        self.booking_status = booking_status
    
    def __repr__(self):
        return f"Booking({self.id}, {self.host_id}, {self.guest_id}, {self.space_id}, {self.booking_date}, {self.booking_status})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__