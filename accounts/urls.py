from django.urls import path

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import Dashboard, SignupView, SigninView

app_name = 'accounts'  
urlpatterns = [
    path('', Dashboard, name='home'),
    path('signin/', SigninView.as_view(), name='login_Accounts'),
    path('signup/', SignupView.as_view(), name='signup'),


    ]
