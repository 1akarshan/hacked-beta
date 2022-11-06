from django.db import models
import base64

#
# class ASLQuestions(models.Model):
#
#     qkey = models.BigAutoField(primary_key=True)
#     question = models.TextField()
#     option1 = models.IntegerField()
#     option2 = models.IntegerField()
#     correct_option = models.TextField(choices=OPTION_CHOICES)
#

# class ASLOptions(models.Model):
#     option_id = models.BigAutoField(primary_key=True)
#     option_text = models.TextField()
#    sign_id = models.IntegerField(default=None)
#
class VideoCapture(models.Model):
    video_id = models.BigAutoField(primary_key=True)

    _data = models.TextField(
        db_column='data',
        blank=True)

    def set_data(self):
        return self._data.removeprefix("data:video/mp4;base64,")

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)
