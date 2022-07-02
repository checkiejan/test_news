from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'stories/index.html')


def blog(request):
    return render(request, 'stories/blog.html')


def single(request):
    return render(request, 'stories/single.html')


def contact(request):
    return render(request, 'stories/Contact_us.html')
