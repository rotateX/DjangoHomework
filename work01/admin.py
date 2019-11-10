from django.contrib import admin
from work01.models import Article, Category, Tag
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'pub_time', 'views')
    list_per_page = 5
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')




admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)