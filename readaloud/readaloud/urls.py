from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from fbv.views import html_view
from markdownx import urls as markdownx


urlpatterns = [
    path("admin/", admin.site.urls),
    path("book/", include("book.urls")),
    path("", html_view, {"template_name": "front.html"}),
    path("markdownx/", include(markdownx)),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),]
