# Create sets
python_students = {"Asha", "Rahul", "Neha"}
data_science_students = {"Rahul", "Vikram", "Meera"}

# Add a new student to Python
python_students.add("Kiran")

# Remove a student from Data Science
data_science_students.remove("Vikram")

# Students in both courses (intersection)
both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)

# Students only in Python (difference)
only_python = python_students - data_science_students
print("Students only in Python:", only_python)

# All students (union)
all_students = python_students | data_science_students
print("All students:", all_students)

# Dictionary with course names and student counts
course_dict = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

# Loop to print course details
for course, count in course_dict.items():
    print("Course: {}, Students: {}".format(course, count))

# Dictionary comprehension (double values)
growth_dict = {course: count * 2 for course, count in course_dict.items()}
print("Expected growth:", growth_dict)