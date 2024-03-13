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
    
    path('ticket/<int:ticket_id>/', views.print_ticket, name='print_ticket'),
    path('print-ticket/', views.print_ticket, name='print_ticket'),
    path('save_ticket/', views.save_ticket, name='save_ticket'),
    path('book-ticket/<int:schedule_id>/', views.book_ticket, name='book_ticket'),
    path('ticket_confirmation/', views.ticket_confirmation, name='ticket_confirmation'),

]
