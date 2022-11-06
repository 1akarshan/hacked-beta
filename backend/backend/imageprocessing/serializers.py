from rest_framework.serializers import Serializer, FileField, ModelSerializer

from imageprocessing.models import VideoCapture


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']


class BlobSerializer(ModelSerializer):
    class Meta:
        model = VideoCapture
        fields = '__all__'
