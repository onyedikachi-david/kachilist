from django.shortcuts import render
import request
from bs4 import BeautifulSoup


# Create your views here.

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_front_end = {
        'search': search,
    }
    return render(request, 'kachilist/new_search.html', stuff_for_front_end)
