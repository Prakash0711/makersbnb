import os
from flask import Flask, request, render_template, redirect, flash, jsonify, url_for, session
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User
from lib.booking import Booking
from lib.booking_repository import BookingRepository


app = Flask(__name__)
app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))