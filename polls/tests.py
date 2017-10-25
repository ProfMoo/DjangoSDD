import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		'''
		ensures that questions published with a future date gets a false
		from was_published_recently()
		'''
		time = timezone.now() + datetime.timedelta(days = 30)
		future_question = Question(pub_date = time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		'''
		ensures that questions published with a date that is older
		than a day gets a false from was_published_recently()
		'''
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date = time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		'''
		ensures that questions published within the past 24 hours
		get a true from was_published_recently()
		'''
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59,  seconds=59)
		recent_question = Question(pub_date = time)
		self.assertIs(recent_question.was_published_recently(), True)