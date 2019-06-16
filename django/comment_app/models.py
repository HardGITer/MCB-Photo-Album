from datetime import date
from django.db import models
from user_app.models import User


class Comment(models.Model):
    """ stores comments """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(default=date.today)
    content = models.TextField()
