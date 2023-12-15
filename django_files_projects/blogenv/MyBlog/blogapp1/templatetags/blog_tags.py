from django.db.models import Count
from django import template
from ..models import Post

#
register=template.Library()
@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('post/latest_posts.html')
def show_latest_posts(count=5):
    recent=Post.published.order_by('-publish')[:count]
    return {'recent':recent}


@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]