from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='AboutPage'),
    path('contact/', views.contact, name='Contact'),
    path('profile/', views.profileCard, name='ProfileCard'),
    path('privacy/', views.privacy, name='Privacy'),
]