from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150,label="Sarlavha")
    content = forms.CharField(label="Yangilik matni",required=False)
    is_published = forms.BooleanField(label="Chop qilinganligi",initial=True)
    category = forms.ModelChoiceField(label="Kategoriya",empty_label='Kategoriyani tanlang',queryset=Category.objects.all())