# -*- coding: utf-8 -*-
# author: itimor

from django.conf import settings
from django.contrib.sites.models import Site
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
import markdown

from models import Blog


class BaseMixin(object):
    paginate_by = settings.PAGE_SIZE

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            context['hot_article_list'] = Blog.objects.filter(published=True).order_by("-view_count")[0:10]
            # context['man_list'] = get_user_model().objects.annotate(Count("post"))
            context['man_list'] = get_user_model().objects.raw(
                'select *, COUNT(post.id) as counts from blog_user as user LEFT JOIN blog_post post ON post.status=1 and post.author_id=user.id GROUP BY user.id');
        except Exception as e:
            print(e)

        return context


class IndexView(BaseMixin, ListView):
    """
    首页
    """
    template_name = 'index.html'
    context_object_name = "posts"
    queryset = Blog.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['carousel_page_list'] = Carousel.objects.all()

        return context


class BlogDetailView(DetailView):
    """
    文章详情
    """
    template_name = "post.html"
    context_object_name = "post"
    queryset = Blog.objects.filter(published=True)

    def get_object(self, queryset=None):
        context = super(BlogDetailView, self).get_object(queryset)

        if not context.published:
            raise PermissionDenied

        # 阅读数增1
        context.access_count += 1
        context.save(modified=False)
        context.content = markdown.markdown(context.content,
                                            extensions=[
                                                'markdown.extensions.abbr',
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.attr_list',
                                                'markdown.extensions.def_list',
                                                'markdown.extensions.toc',
                                                'markdown.extensions.smart_strong',
                                            ])
        return context

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        current_post = context.get("object")

        current_site = Site.objects.get_current()
        page = dict()
        page['comments'] = True
        page['title'] = current_post.title
        page['permalink'] = "http://" + current_site.domain + current_post.get_absolute_url()
        page['path'] = current_post.get_absolute_url
        context['page'] = page

        prev_post = None
        next_post = None

        try:
            prev_post = Blog.objects.get(published=True, pk=(current_post.id - 1))
        except Exception as e:
            print e

        try:
            next_post = Blog.objects.get(published=True, pk=(current_post.id + 1))
        except Exception as e:
            print e

        context['prev_post'] = prev_post
        context['next_post'] = next_post
        return context
