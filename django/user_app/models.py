from django.db import models


class User(models.Model):
    """ stores comments """
    user_id = models.TextField()
