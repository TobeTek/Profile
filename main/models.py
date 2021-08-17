from django.db import models

# Create your models here.

class Response(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	feedback = models.TextField()

	def __str__(self):
		return self.name