# from django.contrib.auth.models import User
# from .models import PostCategory, Post
from .models import Post
from rest_framework import viewsets
# from .serializers import PostCategorySerializer, PostSerializer
from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404


# class PostCategoryViewSet(viewsets.ModelViewSet):
#     queryset = PostCategory.objects.all()
#     serializer_class = PostCategorySerializer

#     def get_queryset(self):
#         if is_authenticated(self.request.user):
#             return PostCategory.objects.filter(created_by=self.request.user)
#         else:
#             return PostCategory.objects.filter(created_by=0)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        if is_authenticated(self.request.user):
            return Post.objects.filter(created_by=self.request.user)
        else:
            return Post.objects.filter(created_by=0)


def is_authenticated(user):
    '''

    Django 2.0: 'bool' object is not callable is_authenticated #218
    https://github.com/juanifioren/django-oidc-provider/issues/218#issuecomment-349220098

    '''
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated
