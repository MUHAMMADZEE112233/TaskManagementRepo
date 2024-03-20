from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

default_router = DefaultRouter()
default_router.register('', TaskViewSet)

urlpatterns = [
    path('', include(default_router.urls)),
]
