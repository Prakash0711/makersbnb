class Space:
    def __init__(self, space_id, address, city, description, price, host_id):
        self.space_id = space_id
        self.address = address
        self.city = city
        self.description = description
        self.price = price
        self.host_id = host_id

    def __repr__(self):
        return f"Space({self.space_id}, {self.address}, {self.city} {self.description}, {self.price}, {self.host_id})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
