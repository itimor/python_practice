# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from blog.models import Blog, Tag, Category


class BlogFilter(filters.FilterSet):
    class Meta:
        model = Blog
        fields = {
            'slug': ['exact', 'contains'],
            'tags__title': ['contains'],
            'category__title': ['exact'],
            'content': ['exact', 'contains'],
            'access_count': ['exact', 'gt'],
            'published': ['exact'],
            'publish_time': ['exact', 'gt'],
        }


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'title': ['exact', 'contains'],
        }


class TagFilter(filters.FilterSet):
    class Meta:
        model = Tag
        fields = {
            'title': ['exact', 'contains'],
        }
