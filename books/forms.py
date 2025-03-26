from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genre", "availability_status"]  # Remove "book_id" if not in model
