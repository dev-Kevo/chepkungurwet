from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:pk>/', views.gallery_detail, name='gallery_detail'),
]