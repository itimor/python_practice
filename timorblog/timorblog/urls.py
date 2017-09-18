# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from timorblog import settings
from django.conf.urls.static import static

from api.blog.views import BlogViewSet, TagViewSet, CategoryViewSet, FriendViewSet, IndexBackgroundViewSet

router = DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'tag', TagViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'friend', FriendViewSet)
router.register(r'bgimg', IndexBackgroundViewSet)


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
