from django import forms
from .models import Category,News
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
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

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Foydalanuvchi nomi",help_text='Foydalanuvchi nomi 150 ta belgidan oshmasligi kerak', widget=forms.TextInput(attrs={'class':'form-control', 'autocomplate': 'off'}))
    email = forms.EmailField(label="e-mail", widget=forms.EmailInput(attrs={'class':'form-control','autocomplate':'off'}))
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Parolni tasdiqlash", widget=forms.PasswordInput(attrs={'class':'form-control'}))



    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Foydalanuvchi nomi", widget=forms.TextInput(attrs={'class':'form-control', 'autocomplate':'off'}))
    password = forms.CharField(label="Parol",widget=forms.PasswordInput(attrs={'class':'form-control','autocomplate':'off'}))

class ContactForm(forms.Form):
    subject = forms.CharField(label="Mavzu", widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label="Matn", widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
