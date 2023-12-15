from django.db.models import Count
from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.core.mail import send_mail
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger)
from django.conf import settings
from .forms import EmailPostForm,CommentForm
from taggit.models import Tag

# Create your views here.

    
def post_list(request,tag_slug=None):
    posts=Post.published.all()
    object_list=Post.published.all()
    tag=None
    if tag_slug:
     tag=get_object_or_404(Tag,slug=tag_slug)
     object_list=object_list.filter(tags__in=[tag])

     
    paginator=Paginator(object_list,2) # two pages to be displayed
    page=request.GET.get('page')
    try:
         posts=paginator.page(page)
    except PageNotAnInteger:
         # if page is not an integer deliver first page
         posts=paginator.page(1)
    except EmptyPage:
         # If page is out of range deliver last page of results
         posts=paginator.page(paginator.num_pages)

    return render(request,'post/list.html',{'posts':posts,'page':page,'tag':tag})


def post_detail(request, year,month,day, post):
     post = get_object_or_404(Post, slug=post,
         status='published',
         publish__year=year,
         publish__month=month,
         publish__day=day)
          
     # adding Commenting system
     # active comments
      
     comments=post.comments.filter(active=True)
     new_comment=None
     if request.method=='POST':
          comment_form=CommentForm(data=request.POST)

          if comment_form.is_valid():
               # create a new comment object but not yet save to DataBase
               new_comment=comment_form.save(commit=False)
               new_comment.post=post
               new_comment.save()
     else:
          comment_form=CommentForm()
               # retrieving data with similar tags

     post_tags_ids=post.tags.values_list('id', flat=True)
     similar_posts=Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
     similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

     
     return render(request,'post/detail.html',{'post': post,
                                               'comments':comments,
                                               'comment_form':comment_form,
                                               'new_comment':new_comment,
                                               'similar_posts':similar_posts
                                           })


  





# we are SENDING OUR POST VIA AN EMAIL 
def post_share(request,post_id):
     # To successfully send the e-mail, you will can use SMTP server by installing
     # pip install python-decouple or use 
     # retrieve post by id
     post_form=get_object_or_404(Post, id=post_id,status='published')
     sent=False

     if request.method=='POST':
          # form was submitted
          form=EmailPostForm(request.POST)
          if form.is_valid():
               # Form fields passed validation
               cd=form.cleaned_data
               post_url=request.build_absolute_uri(post_form.get_absolute_url())
               subject=f"{cd['yourName']} recommends you read {post_form.title}"
               email_from=settings.EMAIL_HOST_USER
               message=f"Read {post_form.title} at {post_url}\n\n {cd['yourName']}\'s comments: {cd['comments']}"
               send_mail(subject,message,email_from, [cd['receiver']])
            #   send_mail(
              #   'That’s your subject',
              #   'That’s your message body',
             #    'from@yourdjangoapp.com',
             #    ['to@yourbestuser.com'],
            #     fail_silently=False,
            #     )
               sent=True
     else:
          form=EmailPostForm()
     return render(request,'post/share.html',{'post_form':post_form,'form':form,'sent':sent})





