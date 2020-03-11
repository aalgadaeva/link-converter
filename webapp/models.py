from django.db import models


class Converter(models.Model):
    link = models.URLField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=155, default=True)

    REQUIRED_FIELDS = ['email']
