from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TestDataViewSet

router = DefaultRouter()
router.register('', TestDataViewSet, basename='test')

urlpatterns = router.urls