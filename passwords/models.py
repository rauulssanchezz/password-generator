from django.db import models

class GeneratedPassword(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    password_name = models.CharField()
    password = models.CharField()
