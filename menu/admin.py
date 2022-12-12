from django.contrib import admin
from .models import Breakfast, Lunch, Dinner

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'is_special_menu')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')
    list_editable = ('is_published', 'is_special_menu')
    list_per_page = 10


admin.site.register(Breakfast, MenuAdmin)
admin.site.register(Lunch, MenuAdmin)
admin.site.register(Dinner, MenuAdmin)
