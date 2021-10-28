import datetime

from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='uploads/team_avatars/')
    facebook_link = models.URLField(max_length=300)
    linkedin_link = models.URLField(max_length=300)
    twitter_link = models.URLField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
