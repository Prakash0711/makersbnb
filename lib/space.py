class Space:
    def __init__(self, space_id, address, description, price, host_id):
        self.space_id = space_id
        self.address = address
        self.description = description
        self.price = price
        self.host_id = host_id
        

    def __repr__(self):
        return f"Space({self.space_id}, {self.address}, {self.description}, {self.price}, {self.host_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__