class User():
    def __init__(self, id, username, user_password, email, full_name):
        self.id = id
        self.username = username
        self.user_password = user_password
        self.email = email
        self.full_name = full_name

    def __eq__(self, other):
        return self.__dict__==other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.user_password}, {self.email}, {self.full_name})"