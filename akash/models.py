from django.db import models



class Studymaterial(models.Model):
    title = models.CharField(max_length=500,null=True)
    content = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.title
