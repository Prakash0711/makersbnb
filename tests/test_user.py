from lib.user import User

"""
check existance
"""
def test_user_constructor():
    new_guy = User(444, "handle1", "123456trewq", "someguy@example.com", "John Smith")
    assert new_guy.id == 444
    assert new_guy.username == "handle1"
    assert new_guy.user_password == "123456trewq"
    assert new_guy.email == "someguy@example.com"
    assert new_guy.full_name == "John Smith"

"""
two users with same information compare ads equals
"""
def test_user_equality():
    new_guy_1 = User(74, "handle1", "123456trewq", "someguy@example.com", "John Smith")
    new_guy_2 = User(74, "handle1", "123456trewq", "someguy@example.com", "John Smith")
    assert new_guy_1 == new_guy_2

"""
user objects print in a readable format 
"""
def test_user_formatting():
    new_guy = User(88, "handle1", "123456trewq", "someguy@example.com", "John Smith")
    assert str(new_guy) == 'User(88, handle1, 123456trewq, someguy@example.com, John Smith)'