from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GamePost(models.Model):

	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	description = models.TextField(blank=True,null=True)
	like_count = models.IntegerField(default=0,blank=True,null=True)
	dislike_count = models.IntegerField(default=0,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.description


class Reply(models.Model):

	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	description = models.ForeignKey(GamePost, on_delete=models.CASCADE, null=True)
	reply = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.user.username

