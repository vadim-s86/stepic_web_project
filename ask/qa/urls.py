from django.conf.urls import patterns, include, url

from qa.views import test


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.home', name='home'),
    url(r'login/.*$', test, name='login'),
    url(r'signup/.*$', test, name='signup'),
    url(r'question/[0-9]+/$', 'qa.views.question', name='question'),
    url(r'ask/.*$', test, name='ask'),
    url(r'popular/.*$', 'qa.views.popular', name='popular'),
    url(r'new/.*$', test, name='new'),
)
