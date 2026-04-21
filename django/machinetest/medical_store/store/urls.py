from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 📋 Home page (medicine list)
    path('', views.medicine_list, name='medicine_list'),

    # ➕ Add medicine
    path('add/', views.add_medicine, name='add_medicine'),

    # ✏️ Edit
    path('edit/<int:id>/', views.edit_medicine, name='edit_medicine'),

    # 🗑️ Delete
    path('delete/<int:id>/', views.delete_medicine, name='delete_medicine'),

    # 🔐 Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]