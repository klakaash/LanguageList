from django.db import models

class Language(models.Model):
    name= models.CharField(max_length=50)
    paradign=models.CharField(max_length=50)
    
