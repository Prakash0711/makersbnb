from lib.space import Space


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from spaces")
        spaces = []
        for row in rows:
            space = Space(
                row["id"],
                row["address"],
                row["city"],
                row["description"],
                row["price"],
                row["host_id"],
            )
            spaces.append(space)
        return spaces

    def add(self, space):
        rows = self._connection.execute(
            "INSERT INTO spaces (address, city, description, price, host_id) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            [space.address, space.city, space.description, space.price, space.host_id],
        )

    def find_space(self, id_to_find):
        query = self._connection.execute(
            "SELECT * FROM spaces WHERE id = %s", [id_to_find]
        )
        return Space(
            query[0]["id"],
            query[0]["address"],
            query[0]["city"],
            query[0]["description"],
            query[0]["price"],
            query[0]["host_id"],
        )

    def filtered_space(
        self,
        city=None,
        min_price=None,
        max_price=None,
        check_in_date=None,
        check_out_date=None,
    ):
        query = """
        SELECT s.* FROM spaces s
        WHERE s.id NOT IN (
            SELECT space_id FROM bookings
            WHERE booking_status = 'approved'
            AND (
                (booking_date <= %s AND booking_date + INTERVAL '1 day' >= %s)
            )
        )
        """
        filters = [check_in_date, check_out_date]

        # Exact match on city if provided
        if city:
            query += " AND s.city = %s"
            filters.append(city)

        # Filter by price range if provided
        if min_price:
            query += " AND s.price >= %s"
            filters.append(min_price)
        if max_price:
            query += " AND s.price <= %s"
            filters.append(max_price)

        # Execute the query with the provided filters
        rows = self._connection.execute(query, tuple(filters))
        spaces = []
        for row in rows:
            space = Space(
                row["id"],
                row["address"],
                row["city"],
                row["description"],
                row["price"],
                row["host_id"],
            )
            spaces.append(space)
        return spaces
