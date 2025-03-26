from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_book, name="add_book"),
    path("view/", views.view_books, name="view_books"),
    path("search/", views.search_book, name="search_book"),
    path("update/<int:book_id>/", views.update_book, name="update_book"),
    path("delete/<int:book_id>/", views.delete_book, name="delete_book"),
    
    path("", views.home, name="home"),  # Map "/" to home page
]

