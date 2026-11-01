from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookForm
from books.models import Book


def books_list(request: HttpRequest) ->HttpResponse:
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/books_list.html', context)

def books_home(request: HttpRequest) -> HttpResponse:

    return render(request, 'books/books_home.html')

def books_details(request:HttpRequest, pk) ->HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/books_details.html', context)

def book_create(request:HttpRequest) ->HttpResponse:
    form = BookForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('books:home')
    contex = {
        'form':form
    }
    return render(request, 'books/book_create.html', contex)

