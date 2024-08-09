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