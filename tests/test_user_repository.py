from lib.user_repository import UserRepository
from lib.user import User

"""
# cRud
find user
"""
def test_find_specific_user(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repo = UserRepository(db_connection)
    assert repo.find_user_by_id(1) == User(1, "john_doe", "password123", "john@example.com", "John Doe")


"""
# Crud
create user
"""
def test_create_new_user(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repo = UserRepository(db_connection)
    new_guy = User(None, "handle1", "123456trewq", "someguy@example.com", "John Doe")
    repo.add_user(new_guy)
    assert repo.find_user_by_id(5) == User(5, "handle1", "123456trewq", "someguy@example.com", "John Doe")