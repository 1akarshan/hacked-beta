from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet, VideoCaptureHandler

router = routers.DefaultRouter()
router.register(r'upload-file', UploadViewSet, basename="upload-file")

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', VideoCaptureHandler.as_view()),
    # path('upload/', postVideo, name="upload-video")
    # path('progress/', ProgressResponseViewSet)
]
