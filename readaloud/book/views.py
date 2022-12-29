from django.shortcuts import render

from fbv.decorators import render_html

@render_html()
def index(request):
    return {}
