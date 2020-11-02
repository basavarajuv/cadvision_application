from django.conf.urls import url
from gameapp import views

app_name = 'gameapp'

urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^game_post/$',views.game_post,name='game_post'),
    url(r'^like_count/(?P<id>\d+)/$',views.like_count,name='like_count'),
    url(r'^dislike_count/(?P<id>\d+)/$',views.dislike_count,name='dislike_count'),
    url(r'^post_reply/(?P<id>\d+)/$',views.post_reply,name='post_reply'),
    url(r'^get_reply/(?P<id>\d+)/$',views.get_reply,name='get_reply'),
]
