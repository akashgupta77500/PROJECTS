from django.db import models


class Resume(models.Model):

    resume = models.FileField(null=True)

    def __str__(self):
        return str(self.id)