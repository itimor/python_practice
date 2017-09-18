# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from blog.models import Blog, Tag, Category, Friend, IndexBackground

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='title')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='title')

    class Meta:
        model = Blog
        fields = ['url', 'id', 'title', 'slug', 'img_upload', 'content', 'published', 'access_count', 'publish_time', 'add_time', 'tags', 'category']
        read_only_fields = ('publish_time', )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'id', 'title']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'title']


class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ['url', 'id', 'title', 'link', 'position', 'active']


class IndexBackgroundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndexBackground
        fields = ['url', 'title', 'img_upload']
