from django.db import models

class dirTree(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    parent = models.IntegerField(default=0)
    ftype = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def distinct_paths(self):
        return self.objects.order_by('path').distinct('path')

    def files_from_path(self, path):
        return self.filter(path__exact=path,ftype__exact='f').order_by('id')

    def dirs_from_path(self, path):
        return self.filter(path__exact=path,ftype__exact='d').order_by('id')

