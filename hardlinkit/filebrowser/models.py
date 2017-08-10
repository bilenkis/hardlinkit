from django.db import models

class dirTree(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    parent = models.IntegerField(default=0)
    ftype = models.CharField(max_length=200)
    def __str__(self):
        return self.name

