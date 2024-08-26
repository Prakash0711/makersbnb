from lib.space import Space

"""
I want to check that a space object is created
Has id, address, description, host_id price
"""

def test_space_exists():
    my_space = Space(1, "3 Buckingham Palace", "Comfy little castle", 99999.99, 2)
    assert my_space.space_id == 1
    assert my_space.address == "3 Buckingham Palace"
    assert my_space.description == "Comfy little castle"
    assert my_space.price == 99999.99
    assert my_space.host_id == 2
    

"""
I want to see if the space object formats nicely
"""

def test_format_string():
    my_space = Space(1, "3 Buckingham Palace", "Comfy little castle", 99999.99, 2)
    assert str(my_space) == "Space(1, 3 Buckingham Palace, Comfy little castle, 99999.99, 2)"


"""
I want to see if both spaces are identical
"""

def test_spaces_equal():
    space1 = Space(1, "3 Buckingham Palace", "Comfy little castle", 99999.99, 2)
    space2 = Space(1, "3 Buckingham Palace", "Comfy little castle", 99999.99, 2)
    assert space1 == space2