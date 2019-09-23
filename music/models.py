from django.db import models
from datetime import date

# Create your models here.
class Songs(models.Model):
    
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)
    pubdate = models.DateField(default=date.today)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
