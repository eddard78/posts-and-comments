from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from user.models import User
from .permissions import IsPostOwnerOrReadOnly, IsCommentOwnerOrReadOnly



class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.prefetch_related()
    lookup_field = 'pk'
    permission_classes = (IsPostOwnerOrReadOnly,)

    
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Post.objects.filter(author=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsCommentOwnerOrReadOnly, )
