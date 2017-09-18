# -*- coding: utf-8 -*-
# author: itimor

import datetime
import re
from django.db import models
from uuslug import slugify
from storage import ImageStorage, BackgroundStorage


class Blog(models.Model):
    title = models.CharField(u'标题', max_length=150, db_index=True, unique=True)
    slug = models.SlugField(u'链接', default='', null=True, blank=True)
    img_upload = models.ImageField(u'封面', upload_to='cover',  blank=True, storage=ImageStorage())
    content = models.TextField(u'内容', )

    add_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    publish_time = models.DateTimeField(u'发布时间', null=True)
    update_time = models.DateTimeField(u'修改时间')
    published = models.BooleanField(u'发布', default=True)

    access_count = models.IntegerField(u'浏览量', default=1, editable=False)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE, verbose_name=u'所属分类')
    tags = models.ManyToManyField('Tag', related_name='posts', verbose_name=u'标签', null=True, blank=True)

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
        ordering = ['-update_time']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        modified = kwargs.pop("modified", True)
        if modified:
            self.update_time = datetime.datetime.utcnow()
        if self.published and self.publish_time == None:
            self.publish_time = datetime.datetime.utcnow()

        super(Blog, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.title


class Category(models.Model):
    """
    大分类
    """
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = u'文章分类'
        verbose_name_plural = u'文章分类'

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    """
    小标签
    """
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        self.title = re.sub("\s", "", self.title)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

    def __unicode__(self):
        return self.title


class Friend(models.Model):
    """
    友情链接
    """
    title = models.CharField(u'名称', max_length=100, default='')
    link = models.URLField(u'链接', default='')
    position = models.SmallIntegerField(u'位置', default=1)
    active = models.BooleanField(u'激活', default=True)

    class Meta:
        ordering = ['-position']
        verbose_name = u'友情链接'
        verbose_name_plural = '友情链接'

    def __unicode__(self):
        return self.title


class IndexBackground(models.Model):
    """
    相册背景图片的数据模型
    """
    title = models.CharField(max_length=20, verbose_name=u'背景名')
    img_upload = models.ImageField(u'图片上传路径', upload_to='background', storage=BackgroundStorage())

    class Meta:
        ordering = ['id']
        verbose_name = u'背景图片'
        verbose_name_plural = u'背景图片'