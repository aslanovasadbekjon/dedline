from django.contrib import admin
from .models import News,Category
from django.utils.safestring import mark_safe

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','updated_at','category','rasmni_olish','is_published')
    list_display_links = ('id','title',)
    search_fields = ('id','title')
    list_editable = ('is_published',)
    list_filter = ('is_published','category')

    fields = ('title','content','created_at','updated_at','category','photo','rasmni_olish','is_published','views')
    readonly_fields = ('rasmni_olish','created_at','updated_at')

    def rasmni_olish(self,obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}">')

    rasmni_olish.short_description = "Rasmi"



admin.site.register(News,NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Sayt adminstratsiyasi'
admin.site.site_header = 'Sayt adminstratsiyasi'