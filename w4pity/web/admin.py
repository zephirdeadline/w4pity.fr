from django.contrib import admin
from .models import *
# Register your models here.


class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subTitle', 'footer')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subTitle', 'date', 'isProject')


class FileAdmin(admin.ModelAdmin):
    list_display = ('path',)


admin.site.register(Site, SiteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(File, FileAdmin)
