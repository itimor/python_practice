# -*- coding: utf-8 -*-
# author: itimor

import datetime
import re
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.core.urlresolvers import reverse
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
    category = models.ForeignKey('Category', verbose_name=u'所属分类')
    tags = models.ManyToManyField('Tag', verbose_name=u'标签', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name=u'作者')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        modified = kwargs.pop("modified", True)
        if modified:
            self.update_time = datetime.datetime.utcnow()
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=(self.id, self.slug))

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model),
                                    args=(self.id,))

    def __unicode__(self):
        return self.title

    def image_view(self):
        return u'<img src="%s" height="200px"/>' % (settings.MEDIA_URL + str(self.img_upload))

    image_view.short_description = '图片展示'
    image_view.allow_tags = True


class Category(models.Model):
    """
    大分类
    """
    title = models.CharField(u'名称', max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['title', ]
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
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

    def __unicode__(self):
        return self.title


class Friend(models.Model):
    """
    友情链接
    """
    title = models.CharField(u'名称', max_length=100, default='')
    url = models.URLField(u'链接', default='')
    position = models.SmallIntegerField(u'位置', default=1)
    active = models.BooleanField(u'激活', default=True)

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = '友情链接'

    def __unicode__(self):
        return self.title


class IndexBackground(models.Model):
    """
    相册背景图片的数据模型
    """
    name = models.CharField(max_length=20, verbose_name=u'背景名')
    img_upload = models.ImageField(u'图片上传路径', upload_to='background', storage=BackgroundStorage())

    def image_view(self):
        return u'<img src="%s" height="500px"/>' % (settings.MEDIA_URL + str(self.img_upload))

    image_view.short_description = '图片展示'
    image_view.allow_tags = True

    class Meta:
        verbose_name = u'背景图片'
        verbose_name_plural = u'背景图片'