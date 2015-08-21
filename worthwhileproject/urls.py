from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worthwhileproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Course.views.index', name='index'),
    url(r'^courses/$', 'Course.views.listView', name='courseList'),

    url(r'^courses/add/$', 'Course.views.addChangeView', name='courseAdd'),

    url(r'^courses/(?P<pk>[0-9]+)/$', 'Course.views.detailView', \
        name='courseDetail'),
    url(r'^courses/(?P<pk>[0-9]+)/change$', 'Course.views.addChangeView', \
        name='courseAdd'),

    url(r'^gallery/$', 'Course.views.gallery', name='gallery'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

