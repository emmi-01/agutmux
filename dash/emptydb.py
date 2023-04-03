from pymongo import MongoClient

# create a client instance
string = "mongodb+srv://test:test@cluster0.dnxuorp.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(string)


db = client.tour_booking_db

# Get a reference to the tour_bookings collection
tour_bookings_collection = db.tour_bookings

# Delete all documents from the tour_bookings collection
result = tour_bookings_collection.delete_many({})

# Print the number of deleted documents
print(f"Deleted {result.deleted_count} documents from the tour_bookings collection")
