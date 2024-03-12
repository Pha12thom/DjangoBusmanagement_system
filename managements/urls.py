from django.urls import path, include
from . import views
urlpatterns = [ 
               
    path('',views.home, name="homepage"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.homepage, name='home'),
    path('search_routes/', views.search_routes, name='search_routes'),
    path('search_form/', views.search_form, name='search_form'),
    path('booking/', views.booking, name='booking'),

]
