from pymongo import MongoClient

# create a client instance
string = "mongodb+srv://test:test@cluster0.dnxuorp.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(string)


db = client.tour_booking_db

tour_bookings_collection = db['tour_bookings']

# iterate through documents and print name and mobile
for booking in tour_bookings_collection.find():
    print(f"Name: {booking['name']}, Mobile: {booking['tel']}")
