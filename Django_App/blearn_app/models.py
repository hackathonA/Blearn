from django.db import models


class TestModel(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
