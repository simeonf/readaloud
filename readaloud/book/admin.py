from django.contrib import admin

from .models import Author, Book, Series

from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Author)
admin.site.register(Book, MarkdownxModelAdmin)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass
