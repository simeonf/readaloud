from django.db import models
from django.urls import reverse

from tagulous.models import TagField
from markdownx.models import MarkdownxField


class Author(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return str(self.name)


class VisibleBookManager(models.Manager):
    def all_visible(self):
        return self.filter(display=True)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    illustrator = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="illustrator_set",
    )
    name = models.CharField(max_length=144)
    slug = models.SlugField(null=False)  # TODO: Needs to be unique
    categories = TagField(blank=True)
    description = MarkdownxField(help_text="Use markdown for formatting")
    year = models.IntegerField()
    age = models.IntegerField(
        blank=True, null=True, help_text="Add an appropriate age for this book."
    )
    goodreads = models.URLField(
        help_text="Add link to goodreads page", blank=True, null=True
    )
    display = models.BooleanField(
        default=True, help_text="Uncheck to hide on the site."
    )
    cover = models.ImageField(blank=True, null=True, upload_to="books/covers/")

    objects = VisibleBookManager()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})


class Series(models.Model):
    title = models.CharField(max_length=144)
    book = models.ManyToManyField(Book)


    class Meta:
        verbose_name_plural = "Series"


    def __str__(self):
        return self.title
