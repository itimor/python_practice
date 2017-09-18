# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from blog.models import Blog, Tag, Category, Friend, IndexBackground
from serializers import BlogSerializer, TagSerializer, CategorySerializer, FriendSerializer, IndexBackgroundSerializer
from filters import BlogFilter, CategoryFilter, TagFilter

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_class = BlogFilter
    ordering_fields = ('access_count',)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_class = TagFilter



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_class = CategoryFilter



class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class IndexBackgroundViewSet(viewsets.ModelViewSet):
    queryset = IndexBackground.objects.all()
    serializer_class = IndexBackgroundSerializer