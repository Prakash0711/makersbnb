from lib.space_repository import SpaceRepository
from lib.space import Space

"""
When we call all, we want to see a list of all the space objects
"""

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Space(1, "123 Main St", "Cozy apartment in the heart of downtown", 100, 1),
        Space(2, "456 Elm St", "Spacious loft with city views", 150, 2),
        Space(3, "789 Oak St", "Charming cottage near the beach", 120, 3),
        Space(4, "321 Pine St", "Modern studio with rooftop access", 80, 4)]

def test_add_space(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repository = SpaceRepository(db_connection)
    space = Space(None, "679 Oxford street", "Not so Cozy apartment in the heart of downtown", 100, 1)
    repository.add(space)
    assert repository.all() == [Space(1, "123 Main St", "Cozy apartment in the heart of downtown", 100, 1),
        Space(2, "456 Elm St", "Spacious loft with city views", 150, 2),
        Space(3, "789 Oak St", "Charming cottage near the beach", 120, 3),
        Space(4, "321 Pine St", "Modern studio with rooftop access", 80, 4),
        Space(5, "679 Oxford street", "Not so Cozy apartment in the heart of downtown", 100, 1)]

"""
when given an id, we get the corresponding space
"""
def test_find_space(db_connection):
    db_connection.seed("seeds/makersbnb_db_test.sql")
    repo = SpaceRepository(db_connection)
    assert repo.find_space(3) == Space(3, "789 Oak St", "Charming cottage near the beach", 120, 3)
    