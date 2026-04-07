# Create sets
frontend_students = {"Asha", "Rahul", "Neha"}
backend_students = {"Rahul", "Vikram", "Meera"}

# Add a new student to Backend
backend_students.add("Kiran")

# Remove a student from Frontend
frontend_students.remove("Neha")

# Students in both courses (intersection)
both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)

# Students only in Backend (difference)
only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)

# Total unique students (union)
all_students = frontend_students | backend_students
print("Total unique students:", len(all_students))

# Dictionary with course counts
course_dict = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

# Print course details
for course, count in course_dict.items():
    print("Course: {}, Students: {}".format(course, count))

# Dictionary comprehension + adding Fullstack
growth_dict = {course: count for course, count in course_dict.items()}
growth_dict["Fullstack"] = course_dict["Frontend"] + course_dict["Backend"]

print("Updated course dictionary:", growth_dict)