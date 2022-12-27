from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=144)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    illustrator = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="illustrator_set"
    )
    name = models.CharField(max_length=144)
    slug = models.SlugField(null=False)  # TODO: Needs to be unique for an owner.
    description = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
