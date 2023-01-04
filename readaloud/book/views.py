from django.shortcuts import render, get_object_or_404

from book.models import Book

from fbv.decorators import render_html


@render_html()
def book_index(request):
    return {"books": Book.objects.all(), "page": "book"}


@render_html()
def book_detail(request, slug):
    return {"book": get_object_or_404(Book, slug=slug), "page": "book"}
