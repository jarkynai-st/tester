from django.db import models

# Create your models here.

class Polls(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField()

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    true_answer = models.CharField(max_length=40)
    poll = models.ForeignKey(Polls,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

class ChoiceAnswer(models.Model):
    variance = models.CharField(max_length=40)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=50)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)