from rest_framework import generics

from .serializers import UploadSerializer, BlobSerializer
from .models import VideoCapture
import base64


class VideoCaptureViewSet(generics.ListCreateAPIView):
    queryset = VideoCapture.objects.all()
    serializer_class = BlobSerializer

    def perform_create(self, serializer):
        VideoCapture.objects.all().delete()
        serializer.save()
        print(serializer.data.keys())
        data = serializer.data['_data']
        fh = open("video.mp4", "wb")
        fh.write(base64.b64decode(data + "=" * (-len(data) % 4)))
        fh.close()
