import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_string = models.CharField(max_length=255)
    publication_date = models.DateTimeField("2024-10-02")
    def __str__(self):
        return self.question_string
    
    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_string = models.CharField(max_length=255)
    nbr_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_string

