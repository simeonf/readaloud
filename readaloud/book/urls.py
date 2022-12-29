from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_index, name="book_index"),
    path('<slug>/', views.book_detail, name="book_detail"),
]
