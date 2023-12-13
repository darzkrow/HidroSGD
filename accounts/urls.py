from django.urls import path

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import InicioView,  Dashboard, SignupView, SigninView, SignoutView

app_name = 'accounts'  
urlpatterns = [
    path('',          InicioView.as_view(), name = 'index'),
    path('dashboard/', Dashboard.as_view(), name='home'),
    path('signin/',    SigninView.as_view(), name='signin'),
    path('signup/',    SignupView.as_view(), name='signup'),
    path('signout/',   SignoutView.as_view(), name='signout'),

    ]
