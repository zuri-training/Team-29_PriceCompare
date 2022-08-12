from django.urls import path
from .views import faq
from .views import profilecard

urlpatterns = [
    path('faq/', faq, name = 'faq' ),
    path('profilecard/', profilecard, name = 'profilecard' )
    
]

    

