from rest_framework import serializers
# from .models import PostCategory, Post
from .models import Post


# class PostCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostCategory
#         fields = ('nama_kategori', 'deskripsi_kategori')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
