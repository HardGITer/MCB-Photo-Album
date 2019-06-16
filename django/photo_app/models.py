from django.db import models
from datetime import date

from page_app.models import Page


class Photo(models.Model):

    image = models.ImageField(upload_to="Images/", default="Images/None/No-img.jpg")
    upload_date = models.DateField(default=date.today)
    page = models.ForeignKey(Page, on_delete=models.PROTECT)
