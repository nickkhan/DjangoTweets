from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from mytweetsrv.models import Tweets, Subscriber
from rest_framework import viewsets, routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class TweetsViewSet(viewsets.ModelViewSet):
    model = Tweets

class SubscriberViewSet(viewsets.ModelViewSet):
    model = Subscriber

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tweets', TweetsViewSet)
router.register(r'subscriber', SubscriberViewSet)
    
urlpatterns = patterns('',
    # Examples:
    url(r'^mytweetsrv-api', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^$', 'mytweetsrv.views.home'),
    url(r'home', 'mytweetsrv.views.home'),
    url(r'register', 'mytweetsrv.views.register'),
    url(r'search', 'mytweetsrv.views.search'),
    url(r'follow', 'mytweetsrv.views.follow'),
    url(r'PostTweet', 'mytweetsrv.views.PostTweet'),
    url(r'unsubscribe', 'mytweetsrv.views.unsubscribe'),
    url(r'login', 'django.contrib.auth.views.login'),
    url(r'logout', 'django.contrib.auth.views.logout'),
    url(r'^CheckIfRefreshNecessary/\d*', 'mytweetsrv.views.CheckIfRefreshNecessary'),
    url(r'^CheckIfRefreshNecessary', 'mytweetsrv.views.CheckIfRefreshNecessary'),
    # url(r'^DjangoTweets/', include('DjangoTweets.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
)
urlpatterns += staticfiles_urlpatterns()