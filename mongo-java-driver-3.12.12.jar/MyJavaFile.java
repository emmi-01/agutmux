import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;
import org.bson.Document;

public class MyJavaFile {

    public static void main(String[] args) {

        // Set up the client settings
        String username = "test";
        String password = "test";
        String cluster = "cluster0.dnxuorp.mongodb.net";
        String databaseName = "tour_booking_db";
        String uri = String.format("mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority", username, password, cluster, databaseName);
        MongoClientSettings settings = MongoClientSettings.builder()
                .applyConnectionString(new ConnectionString(uri))
                .build();

        // Create a client instance
        MongoClient client = MongoClients.create(settings);

        // Get a handle to the tour bookings collection
        MongoDatabase database = client.getDatabase(databaseName);
        MongoCollection<Document> tourBookingsCollection = database.getCollection("tour_bookings");

        // Iterate through documents and print name and mobile
        for (Document booking : tourBookingsCollection.find()) {
            System.out.printf("Name: %s, Mobile: %s%n", booking.getString("name"), booking.getString("tel"));
        }

        // Close the client instance
        client.close();
    }
}

