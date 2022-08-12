from django.urls import path
from .views import contactPage, faq, Home, pricecompare, SearchResultView

urlpatterns = [
    path('faq/', faq, name = 'faq' ),
    path('contact/', contactPage, name = 'contact' ),
    path('home', Home, name='home'),
    path('<int:pk>/', pricecompare, name='compare'),
    path('', SearchResultView.as_view(), name= 'search'),

]