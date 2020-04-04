from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Article
from django.views.decorators.http import require_POST
from .forms import CommentForm
@require_POST
def comment(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(article)
    return render(request,'comment/preview.html',{
        'form':form,'article':article
    })
# Create your views here.
