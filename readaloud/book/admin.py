from django.contrib import admin

from .models import Author, Book

from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Author)
admin.site.register(Book, MarkdownxModelAdmin)
