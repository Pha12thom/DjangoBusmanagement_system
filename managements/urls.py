from django.urls import path, include
from . import views
urlpatterns = [ 
    path('',views.home, name="homepage"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.homepage, name='home'),
    path('search_routes/', views.search_routes, name='search_routes'),
    path('search_form/', views.search_form, name='search_form'),
    path('bus_detail/', views.bus_detail, name='bus_detail'),
    path('bus/<int:bus_id>/', views.bus_detail, name='bus_detail'),
    path('seat_selection/', views.seat_selection, name='seat_selection'),
    path('book_seat/<int:seat_number>/', views.book_seat, name='book_seat'),
    path('confirm_booking/<int:seat_number>/', views.confirm_booking, name='confirm_booking'),
]
