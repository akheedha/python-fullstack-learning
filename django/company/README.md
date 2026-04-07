# 🏢 Company - Employee Directory (Django)

## 📌 Overview

This project is a simple **Employee Directory web application** built using Django.  
It dynamically displays employee information stored in a database and allows management through the Django admin panel.

---

## 🚀 Features

### 👨‍💼 Employee Management

Each employee record contains:
- Name
- Job Title
- Salary
- Employment Type (Full-Time / Part-Time)

---

## 📋 Employee Directory Page (`/`)

- Displays all employees using a loop
- Shows:
  - Name
  - Job Title
  - Salary

---

## 🎯 Conditional Display

- 🟢 **Full-Time employees** → displayed in green  
- 🔴 **Part-Time employees** → displayed in red  

---

## ⚠️ Empty State Handling

- If no employees exist:
  👉 Displays message:  
  **"No employees available."**

---

## 🔧 Admin Panel

- Add, edit, and delete employees using Django Admin
- Access:
  👉 http://127.0.0.1:8000/admin/

---

## 🛠 Tech Stack

- Python
- Django
- HTML
- CSS
- SQLite (default database)

---

## ▶️ How to Run the Project

```bash
# Navigate to project folder
cd django/company

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver