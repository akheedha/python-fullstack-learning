# Create lists for each workshop
web_dev = ["Rahul", "Anu", "Kiran"]
data_science = ["Meera", "Asha", "Vikram"]
ui_ux = ["Riya", "Arjun", "Neha"]

# Combine into nested list
all_participants = [web_dev, data_science, ui_ux]

# Add new participant to Web Development
web_dev.append("Sohan")

# Insert participant at 2nd position in Data Science
data_science.insert(1, "Priya")

# Remove last participant from UI/UX
ui_ux.pop()

# Copy Data Science list and clear original
data_science_copy = data_science.copy()
data_science.clear()

# Display first two Web Development participants
print("First two Web Dev participants:", web_dev[:2])

# List comprehension: length of each name in copied Data Science list
name_lengths = [len(name) for name in data_science_copy]
print("Name lengths (Data Science):", name_lengths)

# Check if "Asha" exists in any workshop
asha_exists = (
    "Asha" in web_dev or
    "Asha" in data_science_copy or
    "Asha" in ui_ux
)
print("Is Asha in any workshop?", asha_exists)

# Tuple of first participant from each workshop
first_participants = (web_dev[0], data_science_copy[0], ui_ux[0])
print("First participants tuple:", first_participants)