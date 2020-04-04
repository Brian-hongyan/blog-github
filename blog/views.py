from django.shortcuts import render,get_object_or_404
from .models import Article,Category

def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',{'articles':articles})
def article_page(request,pk):
    article = get_object_or_404(Article,pk=pk)
    return render(request,'blog/article_page.html',{'article':article})
def archives(request,year,month):
    articles = Article.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    return render(request,'blog/index.html',{'articles':articles})
def categories(request,pk):
    cat = get_object_or_404(Category,pk=pk)
    articles = Article.objects.filter(category=cat).order_by('-created_time')
    return render(request, 'blog/index.html', {'articles': articles})

# Create your views here.
