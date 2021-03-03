from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path('', poll_page, name='poll'),
    path('question/<int:poll_id>/',question_page,name='questions'),
    path('choiceanswer/<int:question_id>/',ChoiceAnswer_page,name='choiceanswer'),
    path('answer/<int:question_id>/',answer_page,name='answer')
]