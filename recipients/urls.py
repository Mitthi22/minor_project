from django.urls import path
from .views import register_recipient, success

urlpatterns = [
    path('register/', register_recipient, name='register_recipient'),
    path('success/', success, name='success'),
]
