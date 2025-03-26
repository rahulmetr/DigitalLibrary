from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("book_id", "title", "author", "genre", "availability_status")  
    list_filter = ("genre", "availability_status")  

