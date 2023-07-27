from django.urls import path
from . import views



urlpatterns = [path('',views.index,name='index'),
              path('specific/', views.specific, name='specific'),
              path('getResponse',views.getResponse, name='getResponse'),
              path('getWeather',views.getWeather,name= 'getWeather'),
               path('getNews',views.getNews,name='getNews')
               
               ]