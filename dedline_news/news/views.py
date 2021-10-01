from django.shortcuts import render,get_object_or_404,redirect
from .models import News, Category
from .forms import NewsForm, UserRegisterForm,UserLoginForm
from django.contrib.auth import login, logout
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

#def index(request):
    # news = News.objects.all()
    # #categories = Category.objects.all()
    # context = {
    #     'news': news,
    #     'title': "Yangilklar ro`yxati",
    #     #'categories': categories,
    #
    # }
    # return render(request,template_name='news/index.html',context=context)

# def get_category(request,category_id):
#     news = News.objects.filter(category_id = category_id)
#    # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         #'categories': categories,
#         'category': category
#     }
#     return render(request, template_name='news/category.html', context = context)

# def view_news(request,news_id):
#     #news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News,pk=news_id)
#     return render(request,'news/view_news.html',{"news_item":news_item})

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #News.objects.create(**form.cleaned_data)
#             form.save()
#             #return redirect('add_news')
#         return render(request, 'news/add_news.html', {'form': form})
#     else:
#         form = NewsForm()
#
#     return render(request, 'news/add_news.html', {'form':form})

#######

class BoshNews(MyMixin,ListView):
    model = News
    template_name = 'news/home_page.html'
    context_object_name = 'news'
    #extra_context = {'title':'Bosh sahifa'}
    mixin_prop = "Hello world"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bosh sahifa'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(MyMixin,ListView):
    model = News
    template_name = 'news/home_page.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

class ViewNews(DetailView):
    model = News
    #pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'

class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url = reverse_lazy('home')
    #login_url = '/admin/'
    #login_url = reverse_lazy('home')
    raise_exeptions = True


def test(request):
    objects = ['a1','a2','a3','a4','a5','a6','a7']
    paginator = Paginator(objects,2)
    page_num = request.GET.get('page',1)
    page_objects = paginator.get_page(page_num)
    return render(request,'news/test.html',{'page_obj':page_objects})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Siz muvaffaqqiyatli ro`yxatdan o`tdingiz")
            return redirect('login')
        else:
            messages.error(request,"Ro`yxatdan o`tishda xatolik")
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('login')