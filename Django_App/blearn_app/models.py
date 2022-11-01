from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=140)
    # blurがかかった単語
    blur_word = models.CharField(max_length=140)
    # blurのかかっていない単語
    word = models.CharField(max_length=140)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

