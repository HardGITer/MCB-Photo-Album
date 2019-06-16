from django.db import models
from photo_album_api.models import PhotoAlbum
from user_app.models import User


class Page(models.Model):
    """ stores pages """
    page_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_album = models.ForeignKey(PhotoAlbum, on_delete=models.CASCADE)
