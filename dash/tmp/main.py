# from flask import Flask, render_template, request
# from pymongo import MongoClient

# app = Flask(__name__)

# string = "mongodb+srv://test:test@cluster0.dnxuorp.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(string)
# db = client["tour_db"]
# collection = db["tour_bookings"]

# @app.route("/")
# def index():
#     bookings = list(collection.find({}))
#     return render_template("index.html", bookings=bookings)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
string = "mongodb+srv://test:test@cluster0.dnxuorp.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(string)
db = client["tour_booking_db"]
tour_bookings_collection = db["tour_bookings"]

@app.route('/book-tour', methods=['POST'])
def book_tour():
    tour_booking = request.get_json()
    tour_bookings_collection.insert_one(tour_booking)
    return {"message": "Tour booked successfully"}


@app.route('/tour-bookings')
def tour_bookings():
    tour_bookings = list(tour_bookings_collection.find().sort("_id", -1))
    return render_template('tour_bookings.html', bookings=tour_bookings)


if __name__ == '__main__':
    app.run(debug=True)
