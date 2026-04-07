import json
from datetime import datetime
from tripdata import get_trip

# Create list of trips
trips = [
    get_trip("Paris", "15-05-2023", "Beautiful city!"),
    get_trip("London", "20-06-2023", "Loved the weather"),
    get_trip("Tokyo", "10-07-2023", "Amazing culture")
]

# Process each trip
for trip in trips:
    # Convert string to date object
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    
    # Format date
    formatted_date = date_obj.strftime("%B %d, %Y")
    
    # Update dictionary
    trip["date"] = formatted_date

# Convert list to JSON string
json_data = json.dumps(trips, indent=4)

# Print JSON
print(json_data)