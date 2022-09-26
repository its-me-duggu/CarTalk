from django.db import models

class contactView(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField()

def __str__(self):
    return self.name
