from django.db import models

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.TextField(default='')
    state = models.BooleanField(default=False)