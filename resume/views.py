from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')


def blogpost1(request):
    return render(request, 'blogpost1.html')


def portfolio1(request):
    return render(request, 'portfolio1.html')
