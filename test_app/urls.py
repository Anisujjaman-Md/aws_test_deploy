from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CeleryTaskView, ServerStatus

router = DefaultRouter()
# router.register('', ServerStatus, basename='test')

urlpatterns = [
    path('', ServerStatus.as_view(), name = "server_test"),
    path('celery-task/', CeleryTaskView.as_view(), name='celery-task')
    
] +router.urls