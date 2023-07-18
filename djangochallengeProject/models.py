from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    Email = models.CharField(max_length=30, blank=False, null=False)
    age = models.CharField(max_length=20, blank=False, null=False)



def __str__(self):
    return self.name