import json
from datetime import datetime
from tracker import create_record

# Create list of travel records
records = [
    create_record("Paris", "Lovely trip", "05-06-2022"),
    create_record("Rome", "Historic places", "12-07-2023"),
    create_record("Dubai", "Amazing city", "25-12-2021")
]

# Convert date format
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

# Convert to JSON string
json_data = json.dumps(records, indent=4)
print("JSON Output:\n", json_data)

# Parse JSON back to Python object
parsed_data = json.loads(json_data)

# Display each record
print("\nParsed Records:")
for rec in parsed_data:
    print(f"City: {rec['city']}, Date: {rec['date']}, Comment: {rec['comment']}")