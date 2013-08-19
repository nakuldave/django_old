from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=15)
    author = models.CharField(max_length=100)
    content = models.TextField()
    # age = models.IntegerField()

    def __unicode__(self): # python3 use 'def __str__(self):' instead
        return self.date + ' ' + self.title
