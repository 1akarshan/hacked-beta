import time

from django.core.files.storage import default_storage
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from django.views.decorators.csrf import csrf_exempt


from .serializers import UploadSerializer, BlobSerializer
from .models import VideoCapture
import base64

ML_RESPONSE = [
    {
        "Sign": "Sign (Text)",
        "Accuracy": 0},
    {
        "Sign": "Sign (Text)",
        "Accuracy": 0
    }
]

RESPONSE = {
    "Completed": 0,
}


class TaskManager:
    response = {
        "Completed": 0,
    }

    def __init__(self):
        global RESPONSE
        RESPONSE = self.response

    def detectSign(self):
        global RESPONSE, ML_RESPONSE
        # TODO machine learning call goes here. store to variable ML_RESPONSE
        # ML_RESPONSE = function_name()
        time.sleep(10)
        self.response["Content"] = ML_RESPONSE
        self.response["Completed"] = 1
        RESPONSE = self.response


class VideoCaptureHandler(APIView):

    def post(self, request, format=None):
        print(request)
        VideoCapture.objects.all().delete()
        # serializer = UploadSerializer()
        # if serializer.is_valid():
        #     serializer.save()
        data = request.data['_data']
        fh = open("video.mp4", "wb")
        fh.write(base64.b64decode(data + "=" * (-len(data) % 4)))
        fh.close()
        mode = TaskManager()
        mode.detectSign()
        return Response(RESPONSE)
        # return Response("Video Upload Error!")

#
# class VideoCaptureViewSet(generics.ListCreateAPIView):
#     queryset = VideoCapture.objects.all()
#     serializer_class = BlobSerializer
#
#     def perform_create(self, serializer):
#         VideoCapture.objects.all().delete()
#         data = serializer.data['_data']
#         fh = open("video.mp4", "wb")
#         fh.write(base64.b64decode(data + "=" * (-len(data) % 4)))
#         fh.close()
#         mode = TaskManager()
#         mode.detectSign()
#         return Response(RESPONSE)

# @csrf_exempt
# @api_view(('POST',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def postVideo(request):
#     print(request.POST.keys())
#     if request.method == "POST":
#         try:
#             data = request.POST['_data']
#             fh = open("video.mp4", "wb")
#             fh.write(base64.b64decode(data + "=" * (-len(data) % 4)))
#             fh.close()
#             mode = TaskManager()
#             mode.detectSign()
#             return Response(RESPONSE)
#         except:
#             return Response(RESPONSE)
#
#     return Response("Nothing Here. Post A Video First!")

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "Uploaded a {} file".format(content_type)
        file_name = default_storage.save(file_uploaded.name, file_uploaded)
        return Response(response)

#
# def ProgressResponseViewSet(request):
#     return Response(RESPONSE)
