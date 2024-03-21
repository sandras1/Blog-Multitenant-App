from django.contrib import admin
from . import models
admin.site.register(models.Profile)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'author')

