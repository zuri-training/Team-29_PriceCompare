from django.urls import path
from .views import contactPage, faq

urlpatterns = [
    path('faq/', faq, name = 'faq' ),
    path('contact/', contactPage, name = 'contact' )
]