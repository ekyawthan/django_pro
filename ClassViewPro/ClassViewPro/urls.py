from django.conf.urls import patterns, include, url
from django.contrib import admin
from classViewApp.views import MyView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ClassViewPro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^about/', MyView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
