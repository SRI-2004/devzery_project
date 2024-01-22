

from django.urls import path
from .views import get_profiles

urlpatterns = [
    path('get_profiles/', get_profiles, name='get_profiles'),

]
