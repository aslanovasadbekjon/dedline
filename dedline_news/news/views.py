from django.shortcuts import render,get_object_or_404,redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
