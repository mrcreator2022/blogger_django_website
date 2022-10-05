
from email.policy import default
from enum import unique
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/',default=None)
    blog_slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

    def __str__(self):
        return self.title





