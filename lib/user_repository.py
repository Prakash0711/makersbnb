from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def find_user_by_id(self, id_to_find):
        query = self._connection.execute(
            "SELECT * FROM users WHERE id = %s", [id_to_find]
            )
        return User(
            query[0]['id'],
            query[0]['username'],
            query[0]['user_password'],
            query[0]['email'],
            query[0]['full_name']
            )

    def add_user(self, user_to_add):
        self._connection.execute(
            "INSERT INTO users (username, user_password, email, full_name) VALUES (%s, %s, %s, %s)",
            [user_to_add.username, user_to_add.user_password, user_to_add.email, user_to_add.full_name]
            )
        return None
    
    # Required for login page
    def find_by_username(self, username_to_find):
        query = self._connection.execute(
            "SELECT * FROM users WHERE username = %s", [username_to_find]
        )
        if query:
            return User(
                query[0]['id'],
                query[0]['username'],
                query[0]['user_password'],
                query[0]['email'],
                query[0]['full_name']
            )
        return None