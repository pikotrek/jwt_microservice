from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authx import views

urlpatterns = [
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    path('verify', views.VerifyView.as_view(), name='verify'),
]
