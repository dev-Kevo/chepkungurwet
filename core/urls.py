from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),

    path('subscribe/', views.handle_letter_subscription, name='letter_subscription'),
    path("notify/", views.handle_notify_visitors, name="handle_notify_visitors"),
    path('contact-form/', views.handle_contact_form, name='handle_contact_form'),


    path('404/', views.handle_404, name='handle_404'),
    path('500/', views.handle_500, name='handle_500'),
]