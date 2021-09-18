from django.shortcuts import render
from .models import News,Category
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': "Yangilklar ro`yxati",
        'categories': categories,

    }
    return render(request,template_name='news/index.html',context=context)

