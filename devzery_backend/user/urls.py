from django.urls import path
from .views import get_user_details

urlpatterns = [
    path('user_info/', get_user_details, name='user_info'),
]
