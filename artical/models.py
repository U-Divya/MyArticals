from django.db import models
from PIL import Image


# Create your models here.
class Category(models.Model):
	gname=models.CharField(max_length=20)

	def __str__(self):
		return self.gname

class Blog(models.Model):
	title=models.CharField(max_length=20)
	author=models.CharField(max_length=20)
	publicationdate=models.DateField(auto_now_add=True)
	category=models.ManyToManyField('Category')
	image=models.ImageField(upload_to='image',blank=True,null=True)
	about=models.TextField()

	def __str__(self):
		return self.author