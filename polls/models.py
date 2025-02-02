import datetime

from django.db import models
from django.utils import timezone
from django_mongodb_backend.fields import EmbeddedModelField
from django_mongodb_backend.models import EmbeddedModel


class Poll(models.Model):
    question = EmbeddedModelField("Question")


class Question(EmbeddedModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", null=True)

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
