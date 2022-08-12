from django.urls import path
from .views import faq, Home, PriceCompareView, SearchResultView

urlpatterns = [
    path('faq/', faq, name = 'faq' ),
    path('home', Home, name='home'),
    path('<int:pk>/', PriceCompareView.as_view(), name='compare'),
    path('', SearchResultView.as_view(), name= 'search')

]