from django.urls import path

from .views import contactPage, faq, Home, pricecompare, SearchResultView


from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.landing, name='landing'),
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
    path('<int:pk>/', pricecompare, name='compare'),
    path('', SearchResultView.as_view(), name= 'search'),




]  




