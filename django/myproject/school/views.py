from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Alice", "grade": 85, "passed": True},
        {"name": "Bob", "grade": 40, "passed": False},
        {"name": "Charlie", "grade": 70, "passed": True},
    ]

    return render(request, 'students.html', {'students': students})