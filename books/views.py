from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_books")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})

def view_books(request):
    books = Book.objects.all()
    return render(request, "books/view_books.html", {"books": books})

def search_book(request):
    query = request.GET.get("q", "")
    results = Book.objects.filter(title__icontains=query) | Book.objects.filter(book_id__icontains=query)
    return render(request, "books/search_book.html", {"results": results, "query": query})

def update_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("view_books")
    else:
        form = BookForm(instance=book)
    return render(request, "books/update_book.html", {"form": form, "book": book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("view_books")
    return render(request, "books/delete_book.html", {"book": book})

def home(request):
    books = Book.objects.all()  
    return render(request, "books/home.html", {"books": books})
