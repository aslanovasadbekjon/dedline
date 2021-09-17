from django.shortcuts import render
from .models import News
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Yangilklar ro`yxati",

    }
    return render(request,template_name='news/index.html',context=context)

