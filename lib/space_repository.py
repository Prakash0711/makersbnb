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

    def add_booking(self, guest_id, space_id, check_in_date, check_out_date):
        print(
            f"Guest ID: {guest_id}, Space ID: {space_id}, Check-in: {check_in_date}, Check-out: {check_out_date}"
        )
        self._connection.execute(
            """
            INSERT INTO bookings (host_id, guest_id, space_id, booking_date_start, booking_date_end, booking_status)
            VALUES (
                (SELECT host_id FROM spaces WHERE id = %s), 
                %s, 
                %s, 
                %s, 
                %s, 
                'pending'
            )
            """,
            [space_id, guest_id, space_id, check_in_date, check_out_date],
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
                (booking_date_start <= %s AND booking_date_end >= %s) OR
                (booking_date_start <= %s AND booking_date_end >= %s) OR
                (booking_date_start >= %s AND booking_date_end <= %s)
            )
        )
        """
        filters = [
            check_out_date,
            check_in_date,
            check_out_date,
            check_in_date,
            check_in_date,
            check_out_date,
        ]

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

        print("Query:", query)
        print("Filters:", filters)

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
