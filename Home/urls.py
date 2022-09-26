from xml.etree.ElementInclude import include
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cars',views.cars, name='cars'),
    path('bikes',views.bikes, name='bikes'),
    path('reviews',views.reviews, name='reviews'),
    path('news',views.news, name='news'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
]
