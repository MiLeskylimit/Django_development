from django.db import models

# Create your models here.

# class Users(models.Model):
#     username = models.CharField(max_length=32)
#     name = models.CharField(max_length=16)
#     password = models.CharField(max_length=32)
#     gender = models.IntegerField(default=1)
#     address = models.CharField(max_length=255)
#     phone = models.CharField(max_length=16)
#     email = models.CharField(max_length=50)
#     state = models.IntegerField(default=1)
#     update_date = models.DateTimeField(auto_created=True, auto_now=True)
#     create_data = models.DateTimeField(auto_created=True, auto_now_add=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('Date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
