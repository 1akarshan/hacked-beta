from django.urls import path, include
from rest_framework import routers
from .views import VideoCaptureViewSet


urlpatterns = [

    path('upload/', VideoCaptureViewSet.as_view()),
]
