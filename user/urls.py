from django.urls import path
from .views import CustomUserCreate, ObtainTokenPairWithCustomUserView

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='register'),
    path('login/', ObtainTokenPairWithCustomUserView.as_view(), name='login'),
]
