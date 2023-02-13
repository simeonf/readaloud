from django.shortcuts import get_object_or_404

from book.models import Book

from fbv.decorators import render_html


@render_html()
def book_index(request):
    categories = Book.categories.tag_model
    return {
        "books": Book.objects.all(),
        "page": "book",
        "tags": categories.objects.all(),
    }


@render_html()
def book_detail(request, slug):
    return {"book": get_object_or_404(Book, slug=slug), "page": "book"}
