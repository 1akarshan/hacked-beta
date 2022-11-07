from django.contrib import admin

from .models import ASLQuestions, ASLOptions

admin.site.register(ASLQuestions)
admin.site.register(ASLOptions)