from rest_framework import serializers
from .models import Page


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        madel = Page
        fields = ('id', 'page_owner', 'photo_album')