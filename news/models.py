from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



		

class Category(models.Model):
	name = models.CharField(max_length=225)


	def __str__ (self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	website_url = models.CharField(max_length=255, blank=True, null=True)
	facebook_url = models.CharField(max_length=255, blank=True, null=True)
	twiter_url = models.CharField(max_length=255, blank=True, null=True)
	instagram_url = models.CharField(max_length=255, blank=True, null=True)
	pinterest_url = models.CharField(max_length=255, blank=True, null=True)

	
	def __str__(self):
		return str(self.user)
 	
	def get_absolute_url(self):
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length=225)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
	category = models.CharField(max_length=225, default='Education')
	body = RichTextField(blank=True, null=True)
	title_tag = models.CharField(max_length=225, default="Title tag is for to be displayed instead of title")
	publication_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='blog_post')

	def total_likes(self):
		return self.likes.count()

	def __str__ (self):
		return self.title + "|" + str(self.author)

	def get_absolute_url(self):
		# return reverse('article_detail', args=(str(self.id)))
		return reverse('home')

# Create your models here.
class Comment(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name="comments", on_delete= models.CASCADE)
	
	body = models.TextField()
	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		return '%s-%s' %(self.post.title, self.user)


class Reply(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, related_name="replies", on_delete= models.CASCADE)

	body = models.TextField()
	updated = models.DateField(auto_now=True)
	date_added = models.DateField(auto_now_add=True)


	def __str__(self):
		return str(self.user) + " replied "+ str(self.comment.user)