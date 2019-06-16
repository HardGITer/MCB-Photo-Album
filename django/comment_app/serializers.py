from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        madel = Comment
        fields = ('id', 'user', 'create_date', 'content')
