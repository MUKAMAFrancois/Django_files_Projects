from django import template
from django.db.models import Count
from ..models import Post

register=template.Library()

@register.inclusion_tag('tags/latest_posts.html')
def show_latest_posts(count=5):
    latests=Post.objects.all().order_by('-publish')[:count]
    return {'first_fives':latests}


@register.simple_tag
def most_commented_posts(count=5):
    return Post.objects.all().annotate(total_comments=Count('commented')).order_by('-total_comments')[:count]
