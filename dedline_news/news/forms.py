from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150,label="Sarlavha", widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(label="Yangilik matni",required=False,widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    is_published = forms.BooleanField(label="Chop qilinganligi",initial=True)
    category = forms.ModelChoiceField(label="Kategoriya",empty_label='Kategoriyani tanlang',queryset=Category.objects.all(),widget=forms.Select(attrs={"class":"form-control"}))