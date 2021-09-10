from django.shortcuts import render

def index(request):
    return  render(request, 'dedline_news/index.html')
