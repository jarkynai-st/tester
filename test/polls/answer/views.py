from django.shortcuts import render, redirect

from .forms import AnswerForm
from .models import *
# Create your views here.

def poll_page(request):
    poll = Polls.objects.all()
    context = {"polls":poll}
    return render(request,'answer/polls.html',context)


def question_page(request,poll_id):
    poll = Polls.objects.get(id=poll_id)
    questions = poll.question_set.all()
    context = {"questions":questions,"poll":poll}
    return render(request,'answer/question.html',context)


def ChoiceAnswer_page(request,question_id):
    question = Question.objects.get(id=question_id)
    choiceanswer = question.choiceanswer_set.all()
    context = {"choiceanswer":choiceanswer}
    return render(request,'answer/choiceanswer.html',context)


def answer_page(request,question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choiceanswer_set.all()
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            if question.true_answer == form.cleaned_data['answer']:
                question.poll.points += 1
                question.poll.save()
                return redirect('polls')
    context = {"choices":choices,"questions":question,'form':form}
    return render(request,'answer/answer.html',context)

