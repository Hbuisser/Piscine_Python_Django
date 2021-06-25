from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=128)
	pics = models.ImageField(upload_to='img/')

	def __str__(self):
		return str(self.title)
