from django import forms
from .models import Category,News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        #fields='__all__'
        fields = ['title', 'content','is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),

            'content': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    # title = forms.CharField(max_length=150,label="Sarlavha", widget=forms.TextInput(attrs={"class":"form-control"}))
    # content = forms.CharField(label="Yangilik matni",required=False,widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    # is_published = forms.BooleanField(label="Chop qilinganligi",initial=True)
    # category = forms.ModelChoiceField(label="Kategoriya",empty_label='Kategoriyani tanlang',queryset=Category.objects.all(),widget=forms.Select(attrs={"class":"form-control"}))
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d',title):
            raise ValidationError("Sarlavha raqam bilan boshlanmaydi")
        return title