from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musync.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'api.views.home', name='home'),
    url(r'^song$','api.views.song',name='adminSongPlaylist'),
    url(r'^song_saver$', 'api.views.songs_saver', name='home'),
    url(r'^song2$','api.views.song2',name='0a0minSongPlaylist'),
    url(r'^song_d$','api.views.song_d',name='admainSongPlaylist'),
    url(r'^song2_d$','api.views.song2_d',name='00minSongPlaylist'),
    url(r'^hostedsession$','api.views.hostedsession',name='0a0ssminSongPlaylist'),

)
