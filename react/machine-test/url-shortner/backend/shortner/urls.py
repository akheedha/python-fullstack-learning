from django.urls import path

from .views import (
    signup,
    login,
    create_short_url,
    list_urls,
    update_url,
    delete_url
)

urlpatterns = [

    path(
        'signup/',
        signup
    ),

    path(
        'login/',
        login
    ),

    path(
        'create-url/',
        create_short_url
    ),

    path(
        'list-urls/',
        list_urls
    ),

    path(
        'update-url/<int:id>/',
        update_url
    ),

    path(
        'delete-url/<int:id>/',
        delete_url
    ),
]