from django.urls import path

from .views import (contactPage, faq, 
                    Home, PriceCompareView, SearchResultView, 
                    profilecard, ProductListView, landing_page
)


from . import views
from django.contrib.auth import views as auth_views




app_name = "Haggle"


urlpatterns = [
    path('', landing_page, name='landing' ),
    #AUTHENTICATION
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name ="users\password_reset.html"), name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name ="users\password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ="users\password_reset_form.html"), name='password_reset_confirm'),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name ="users\password_reset_complete.html"), name='password_reset_complete'),
    path('faq/', faq, name = 'faq' ),
    path('contact/', contactPage, name = 'contact' ),
    path('home', Home, name='home'),
    path('privacy/', views.privacy, name='privacy'),


    path('search/', SearchResultView.as_view(), name= 'search'),
    path('profilecard/', profilecard, name = 'profilecard'),
    path('<str:category>/<str:brand>/', ProductListView.as_view(), name= 'product-list'),
    path('<slug>/', PriceCompareView.as_view(), name='compare'),
    


    





]  





