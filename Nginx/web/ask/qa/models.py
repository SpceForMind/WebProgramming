from django.db import models
from django.contrib.auth.models import User

#Manager of model <Question>
class QuestionManager(models.Manager):
	'''
		sort by add date
	'''
	def new(self):
		return self.order_by("-added_at")
	'''
		sort by rating
	'''
	def popular(self):
		return self.order_by("-rating")

class Question(models.Model):
	'''
		field object for access to methods of manager - Question.objects.<method>
	'''
	objects = QuestionManager()
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(blank = True, auto_now_add = True)
	rating = models.IntegerField(default = 0)	
	'''
		<n questions> : <1 user>
	'''
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	'''
		<n questions> : <m users>
		likes is list of users 
		related_name set in other value for avoidong error
		creation question_set for reverse relation
	'''
	likes = models.ManyToManyField(User, related_name = "likes_set")

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank = True, auto_now_add = True)
	'''
		<n answers> : <1 question>
	'''
	question = models.ForeignKey(Question, on_delete = models.DO_NOTHING)
	'''
		<n answers> : <1 author>
	'''
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
