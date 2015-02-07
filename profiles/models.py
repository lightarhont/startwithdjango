from django.db import models
import datetime

class Profiles(models.Model):
    
    class Meta:
        db_table = 'profiles'
    
    userid = models.IntegerField(max_length=11)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    bdate = models.IntegerField(max_length=11)
    biography = models.TextField()
    contacts = models.TextField()
    
    @property
    def fbdate(self):
        dateformat='%m/%d/%Y'
        return str(datetime.datetime.fromtimestamp(self.bdate).strftime(dateformat))
