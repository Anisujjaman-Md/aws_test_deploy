from django.http import Http404
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer

class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)

class ObtainTokenPairWithCustomUserView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer