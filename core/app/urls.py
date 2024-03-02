from django.urls import path 
from app.views import NotificationView

urlpatterns = [
    path('',NotificationView.as_view(), name='main'),
]
