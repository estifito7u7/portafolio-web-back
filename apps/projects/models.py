from django.db import models
from datetime import datetime


from django.conf import settings
# domain = settings.DOMAIN

class Projects(models.Model):

    class Categorys(models.TextChoices):
        react = 'react'
        django = 'django'
        vue = 'vue'
    

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    description = models.TextField()
    category = models.CharField(max_length=50, choices=Categorys.choices, default=Categorys.react)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)  
    website_link = models.URLField(blank=True, null=True)  
    date_created = models.DateTimeField(default=datetime.now)

    def get_thumbnail(self):
        if self.photo:
            return self.photo.url
        return ''

    def __str__(self):
        return self.name