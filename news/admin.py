from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_editable = ('date_published', 'is_published')
    list_display = ('id','title', 'category', 'date_published', 'is_published')
    list_display_links = ('id', 'title', 'category')
    list_per_page = 10
    search_fields = ('title', 'category')


admin.site.register(News, NewsAdmin)