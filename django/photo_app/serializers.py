from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        madel = Photo
        fields = ('id', 'image', 'upload_date', 'page')
