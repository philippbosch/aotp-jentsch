from django.contrib import admin

from music.models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    list_editable = ('order',)

admin.site.register(Track, TrackAdmin)
