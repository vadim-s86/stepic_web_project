from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	QuestionManager = models.Manager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, default='x')
	likes = models.ManyToManyField(related_name='question_like_user')
	def new():
		pass
	def popular():
		pass

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, default='x')
