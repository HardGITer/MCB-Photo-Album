from rest_framework import serializers
from .models import Task, PhotoAlbum


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'content', 'created_on',  'due_date')

        extra_kwargs = {
            'created_by': {'read_only': True}
        }


class PhotoAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        madel = PhotoAlbum
        fields = ('id', 'name', 'description', 'create_date', 'members')