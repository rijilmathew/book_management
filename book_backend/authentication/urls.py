from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/',UserLoginAPIView.as_view(),name='user-login'),
    path('logout/',UserLogoutAPIView.as_view(),name='user-logout'),
    path('userprofile/',UserprofileView.as_view(),name='user-profile'),
    path('userprofile/<int:pk>/', UserProfileRetrieveUpdateAPIView.as_view(), name='userprofile-detail'),
]
