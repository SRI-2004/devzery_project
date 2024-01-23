# authorisation/urls.py
from django.urls import path
from .views import signup, login, forgot_password, reset_password, verify_email

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password/<str:email>/<str:token>/', reset_password, name='reset_password'),
    path('verify_email/<str:email>/<str:token>/', verify_email, name='verify_email'),
]
