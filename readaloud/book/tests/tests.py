from pytest_django.asserts import assertContains, assertNotContains
import pytest

from book.tests.book_factory import BookFactory


@pytest.mark.django_db
def test_goodreads_link_exists(client):
    book = BookFactory(goodreads="http://goodreads.com/url")
    response = client.get(f"/book/{book.slug}/")
    assertContains(response, "http://goodreads.com/url")
    assertContains(response, "Goodreads")


@pytest.mark.django_db
def test_goodreads_link_does_not_exist(client):
    book = BookFactory(goodreads="")
    response = client.get(f"/book/{book.slug}/")
    assertNotContains(response, "Goodreads")
