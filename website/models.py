from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
	slug = models.SlugField(max_length=200, unique=True)
	title = models.CharField(max_length=200, unique=True)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_date = models.DateField(auto_now_add=True)
	preview = models.CharField(max_length=300)
	thumbnail = models.ImageField(upload_to='upload/%Y/%m/%d')
	status = models.IntegerField(choices=STATUS, default=0)


	class Meta:
		ordering = ['-post_date']


	def __str__(self):
		return self.title


class Archive(models.Model):
	slug = models.SlugField(max_length=200, unique=True)
	title = models.CharField(max_length=200)
	blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	year = models.DateField(auto_now=True)


	def __str__(self):
		return self.title
