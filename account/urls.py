from django.urls import path
from .views import ContactMessageView, APIInfoView

urlpatterns = [
    path('contact/', ContactMessageView.as_view(), name='contact'),
    path('info/', APIInfoView.as_view(), name='api_info'),
]
