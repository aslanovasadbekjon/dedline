from django.contrib import admin
from .models import News,Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','updated_at','category','photo','is_published')
    list_display_links = ('id','title',)
    search_fields = ('id','title')
    list_editable = ('is_published',)
    list_filter = ('is_published','category')





admin.site.register(News,NewsAdmin)
admin.site.register(Category)
