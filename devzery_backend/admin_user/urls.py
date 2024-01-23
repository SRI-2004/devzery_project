

from django.urls import path
from .views import get_profiles,logout_view

urlpatterns = [
    path('get_profiles/', get_profiles, name='get_profiles'),
    path('logout/',logout_view,name='logout'),

]
