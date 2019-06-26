from django.db import models

# Create your models here.
class Site(models.Model):
    site_url = models.URLField(max_length=200, null=False)
    shortcut = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.site_url