from django.urls import path
from .views import  form_name_view, test, login


urlpatterns = [
    path('signup/', form_name_view),
    path('login/', login),


]