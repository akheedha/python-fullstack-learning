# Attendance list
attendance = [18, 20, 19, 15, 21]

# Initialize counters
full_days = 0
total_attendance = 0

# Loop through attendance
for day in attendance:
    if day >= 20:
        print(day, "- Full")
        full_days += 1
    else:
        print(day, "- Not Full")
    
    total_attendance += day

# Print results
print("Number of full days:", full_days)
print("Total attendance:", total_attendance)