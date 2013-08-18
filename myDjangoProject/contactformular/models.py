from django.db import models

# Create your models here.

class Meldeformular(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __unicode__(self): # python3 use 'def __str__(self):' instead
        return self.first_name+' '+self.last_name+' (Alter: '+str(self.age)+')'

class Kontaktformular_WTK_Anmeldung(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    # mail = EmailField()
    # gender_w = models.EnumField(w)
    # gender_m = models.Foreigkey(m)

    def __unicode__(self): # python3 use 'def __str__(self):' instead
        return self.first_name+' '+self.last_name+' (Alter: '+str(self.age)+')'

