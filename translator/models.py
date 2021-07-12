from django.db import models

# Create your models here.
class IPA_word(models.Model):
    IPA_string = models.CharField("", max_length=50)