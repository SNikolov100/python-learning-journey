from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book


def landing_page(request: HttpRequest) -> HttpResponse:
    total_books_count = Book.objects.count()
    latest_book = Book.objects.order_by('-published_date').first()

    context = {
        'total_books_count': total_books_count,
        'latest_book': latest_book,
        'page_title': 'Home',
    }
    return render(request, 'books/landing_page.html', context)

def book_list(request: HttpRequest) ->HttpResponse:
    books = Book.objects.all()
    context = {
        'books': books,
        'page_title': 'Dashboard'
    }
    return render(request, 'books/list.html', context)

def book_detail(request: HttpRequest, slug: str) ->HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    context = {
        'book': book,
        'page_title': f'{book.title} details'
    }
    return render(request, 'books/detail.html', context)
