from django.db import models
import base64

#
class ASLQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField()
    difficulty = models.TextField()
    color = models.TextField()
    option1 = models.IntegerField(default=None)
    option2 = models.IntegerField(default=None)
    option3 = models.IntegerField(default=None)
    option4 = models.IntegerField(default=None)
    correct_option = models.IntegerField()



class ASLOptions(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_text = models.TextField()
    link = models.TextField()
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
