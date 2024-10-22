import os
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    flash,
    jsonify,
    url_for,
    session,
)
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)


@app.route("/home", methods=["GET"])
def get_home():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space_list = repository.all()
    return render_template("home.html", spaces=space_list)


def is_logged_in():
    return "user_id" in session


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["user_password"]
        fullname = request.form["full_name"]

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Create user object
        new_user = User(
            id=None,
            username=username,
            user_password=hashed_password,
            email=email,
            full_name=fullname,
        )

        # Save user
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        repository.add_user(new_user)

        flash(f"Welcome! Please login")
        return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["user_password"]

        # Get user from database by email
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        new_user = repository.find_by_username(username)

        if new_user and bcrypt.check_password_hash(new_user.user_password, password):
            # Session management
            session["user_id"] = new_user.id
            session["username"] = new_user.username
            session["full_name"] = new_user.full_name
            flash("Login succesful!")
            return redirect(url_for("userhome"))
        else:
            flash("Invalid input")
    return render_template("login.html")


@app.route("/userhome", methods=["GET"])
def userhome():
    if not is_logged_in():
        flash("Please login first")
        return redirect(url_for("login"))

    return render_template("userhome.html")


@app.route("/search_space", methods=["GET", "POST"])
def search_space():
    if not is_logged_in():
        flash("Please log in first")
        return redirect(url_for("login"))
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()

    if request.method == "POST":
        city = request.form.get("city")
        min_price = request.form.get("min_price")
        max_price = request.form.get("max_price")
        spaces = repository.filtered_space(city, min_price, max_price)

    return render_template("search_space.html", spaces=spaces)


@app.route("/list_space", methods=["GET", "POST"])
def list_space():
    if not is_logged_in():
        flash("Please log in first")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Gather form data
        address = request.form["address"]
        city = request.form["city"]
        description = request.form["description"]
        price = request.form["price"]

        host_id = session["user_id"]

        # Create a Space object
        new_space = Space(
            space_id=None,
            address=address,
            city=city,
            description=description,
            price=price,
            host_id=host_id,
        )

        # Save the new space to the database
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        repository.add(new_space)

        flash("Space listed successfully!")
        return redirect(url_for("userhome"))

    return render_template("list_space.html")


@app.route("/my_bookings", methods=["GET", "POST"])
def my_bookings():
    if not is_logged_in():
        flash("Please log in first")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)

    # Fetch bookings where the user is the host
    requests_received = booking_repo.get_requests_for_host(user_id)

    # Fetch bookings where the user is the guest
    user_bookings = booking_repo.get_bookings_for_user(user_id)

    return render_template(
        "my_bookings.html",
        requests_received=requests_received,
        user_bookings=user_bookings,
    )


@app.route("/update_booking_status/<int:booking_id>", methods=["POST"])
def update_booking_status(booking_id):
    if not is_logged_in():
        flash("Please log in first")
        return redirect(url_for("login"))

    action = request.form.get("action")

    # Map actions to enum values
    if action == "approve":
        status = "approved"
    elif action == "deny":
        status = "denied"
    else:
        flash("Invalid action")
        return redirect(url_for("my_bookings"))

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)

    # Update the booking status in the database
    booking_repo.update(booking_id, status)

    flash(f"Booking has been {status}.")
    return redirect(url_for("my_bookings"))


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
