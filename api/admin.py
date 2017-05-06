from django.contrib import admin

# Register your models here.

from api.models import user , Song , DjSessions , Playlist 


admin.site.register(user)
admin.site.register(Song)
admin.site.register(DjSessions)
admin.site.register(Playlist)