from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-id')

  def popular(self):
    return self.order_by('-rating')

class Question(models.Model):
    object = QuestionManager();
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,  related_name='question_author')
    likes = models.ManyToManyField(related_name='question_like_user')
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.text
