from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=144)

    def __str__(self):
        return str(self.name)


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
    description = models.TextField()
    year = models.IntegerField()
    age = models.IntegerField(blank=True, null=True, help_text="Add an appropriate age for this book.")
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
