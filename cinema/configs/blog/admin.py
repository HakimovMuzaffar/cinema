from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'view', 'created_at', 'updated_at', 'publish', 'rating')
    list_display_links = ('title',)
    list_editable = ('publish',)
    list_filter = ('title', 'category', 'created_at')




admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
