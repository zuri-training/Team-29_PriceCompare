from django.urls import path


from .views import HpCategoryView, DellCategoryView, XiaomiCategoryView, OppoCategoryView, InfinixCategoryView, LenovoCategoryView, SamsungCategoryView, NokiaCategoryView, TechnoCategoryView, ApplePCCategoryView, AsusCategoryView, LenovoPCCategoryView, contactPage, faq, Home, PriceCompareView, SearchResultView, AppleCategoryView


from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    #path('', views.landing, name='landing'),
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

    path('<int:pk>/', PriceCompareView.as_view(), name='compare'),
    path('', SearchResultView.as_view(), name= 'search'),
    path('phone/apple', AppleCategoryView.as_view(), name='apple'),
    path('phone/samsung', SamsungCategoryView.as_view(), name='samsung'),
    path('phone/oppo', OppoCategoryView.as_view(), name='oppo'),
    path('phone/techno', TechnoCategoryView.as_view(), name='techno'),
    path('phone/lenovo', LenovoCategoryView.as_view(), name='lenovo'),
    path('phone/infinix', InfinixCategoryView.as_view(), name='infinix'),
    path('phone/nokia', NokiaCategoryView.as_view(), name='nokia'),
    path('phone/xiaomi', XiaomiCategoryView.as_view(), name='xiaomi'),
    path('laptop/asus', AsusCategoryView.as_view(), name='asus'),
    path('laptop/lenovo', LenovoPCCategoryView.as_view(), name='lenovopc'),
    path('laptop/hp', HpCategoryView.as_view(), name='hp'),
    path('laptop/apple', ApplePCCategoryView.as_view(), name='applepc'),
    path('laptop/dell', DellCategoryView.as_view(), name='dell')

]  





