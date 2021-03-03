from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Polls)
admin.site.register(Question)
admin.site.register(ChoiceAnswer)
admin.site.register(Answer)