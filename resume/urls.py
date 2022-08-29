from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('blogpost1', views.blogpost1, name='blogpost1'),

    path('index2', views.index2, name='index2'),

    path('portfolio1', views.portfolio1, name='portfolio1'),
]