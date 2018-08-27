from django.contrib import admin
from .models import Category, Tags, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_time']
    list_per_page = 10
    search_fields = ['title']
    filter_horizontal = ('tags',)


    # class Media:
    #     js = ('/static/kindeditor-4.1.10/kindeditor-all-min.js',
    #           '/static/kindeditor-4.1.10/lang/zh-CN.js',
    #           '/static/kindeditor-4.1.10/config.js')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagAdmin)
admin.site.register(Article, ArticleAdmin)
