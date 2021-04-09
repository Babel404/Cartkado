from django.db import models
import django.utils.timezone 

class Cartkado(models.Model):

	unique_key = models.CharField(max_length=200, default='-')
	amount = models.FloatField()
	created_at = models.DateTimeField()

	def __str__(self):
		return self.unique_key

class Transaction(models.Model):

	name = models.CharField(max_length=200)
	amount = models.FloatField()
	card_key = models.CharField(max_length=200, default='-')
	created_at = models.DateTimeField()

	def __str__(self):
		return self.card_key +"      DEBITED BY       "+ self.name

