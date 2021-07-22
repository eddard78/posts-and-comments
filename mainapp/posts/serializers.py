from rest_framework import serializers

from posts.models import Post, Comment
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        # read_only_fields = ('author',)

    def create(self, validated_data):
        user = self.context.get('request').user

        post = Post.objects.create(author=user, **validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        data = validated_data.copy()
        data.pop('publication', None)
        for attr, value, in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance