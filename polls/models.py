from django.db import models
from mongoengine import *

class Choice(Document):
	choice_text = StringField(max_length=200)
	votes = IntField(default=0)

	def __unicode__(self):
		return self.choice_text


class Poll(Document):
	question = StringField(max_length=200)
	pub_date = DateTimeField(help_text='date published')
	choices = ListField(ReferenceField(Choice))

	def __unicode__(self):
		return self.question


