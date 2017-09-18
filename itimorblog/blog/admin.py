# -*- coding: utf-8 -*-
# author: itimor

import datetime

from django.contrib import admin
from models import Tag, Blog, Category, Friend, IndexBackground
import os
from django.dispatch import receiver
from django.db import models


# 图片自动删除
@receiver(models.signals.post_delete, sender=Blog)
@receiver(models.signals.post_delete, sender=IndexBackground)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Photo` object is deleted.
    """
    if instance.img_upload:
        if os.path.isfile(instance.img_upload.path):
            os.remove(instance.img_upload.path)


# 图片自动更新
@receiver(models.signals.pre_save, sender=Blog)
@receiver(models.signals.pre_save, sender=IndexBackground)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Photo` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).img_upload
    except sender.DoesNotExist:
        return False

    new_file = instance.img_upload
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'published', 'publish_time', 'access_count')
    list_filter = ('category', 'published', 'publish_time', 'access_count')
    fields = (
        'title',
        'img_upload',
        'content',
        'published',
        'category',
        'tags',
        'image_view'
    )

    exclude = ('publish_time',)
    search_fields = ('title', 'published')
    ordering = ('-add_time', 'published', 'publish_time')
    readonly_fields = ('image_view',)
    list_per_page = 60

    def create_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d')

    create_time.short_description = "创建时间"

    def publish(self, obj):
        if obj.publish_time:
            return obj.publish_time.strftime('%Y-%m-%d')
        else:
            return ''

    publish.short_description = "发布时间"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        if '_save' in request.POST.keys():
            # 只有是操作状态的文章才更新发布时间
            if obj.published:
                obj.publish_time = datetime.datetime.now()
        super(BlogAdmin, self).save_model(request, obj, form, change)
        # obj.save()


class TagAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class FriendAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'position', 'active')


class IndexBackgroundAdmin(admin.ModelAdmin):
    list_display = ('name', 'img_upload',)
    fields = ('name', 'img_upload', 'image_view')
    readonly_fields = ('image_view',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(IndexBackground, IndexBackgroundAdmin)
