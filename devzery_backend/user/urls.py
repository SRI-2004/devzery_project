from django.urls import path
from .views import get_user_details,logout_view

urlpatterns = [
    path('user_info/', get_user_details, name='user_info'),
    path('logout/',logout_view,name='logout'),
]
