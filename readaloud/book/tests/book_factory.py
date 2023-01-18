import factory
from faker import Faker

from book.models import Author, Book

faker = Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.LazyAttribute(lambda _: faker.name())


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    author = factory.SubFactory(AuthorFactory)
    name = factory.LazyAttribute(lambda _: faker.name())
    slug = factory.LazyAttribute(lambda _: faker.name().lower().replace(" ", "-"))
    description = factory.LazyAttribute(lambda _: faker.text())
    year = 2000
    age = 10
