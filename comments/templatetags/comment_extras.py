from django import template
from ..forms import CommentForm
from blog.models import Article
from ..models import comment
register = template.Library()
@register.inclusion_tag('comment/inclusions/_comment_form.html', takes_context=True)
def show_comment_form(context,article,form=None):
    if form is None:
        form = CommentForm()
    return {'form':form,
            'article':article}

@register.inclusion_tag('comment/inclusions/_comments_list.html', takes_context=True)
def show_comments(context,article):
    comments = article.comment_set.all().order_by('-created_time')
    comment_count = comments.count()
    return {
        'comment_count':comment_count,
        'comments':comments,
    }