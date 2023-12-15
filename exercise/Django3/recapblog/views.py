from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import CommentForm, LoginForm


from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage)
#from taggit.models import Tag

# Create your views here.

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, 
                              username=cd['username'],
                              password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('all')
                else:
                    messages.info(request, 'Disabled Account')
                    return redirect('login')
            else:
                messages.info(request, 'Invalid Login')
                return redirect('login')
    else:
        form=LoginForm()  
    return render(request,'accounts/login.html', {'form':form})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Was Taken')
                return redirect('signup')
            else:
                User.objects.create_user(password=password2,username=username,email=email).save()
        else:
            messages.info(request, 'Password Mismatches')
            return redirect('signup')
    return render(request,'accounts/signup.html')

# listing all posts

class Listing_All(ListView):
  #  tags=Tag.objects.all()
    model=Post
 #   context_object_name='all_posts'
    template_name='index.html'
    paginate_by=2

""" def listing_all(request):
    object_list=Post.objects.all()

    paginator=Paginator(object_list,1) # four posts per page
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts=paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts=paginator.page(paginator.num_pages) """
 #   return render(request,'index.html',{'object_list':object_list,'page':page,'posts':posts})


def listing_tech(request):
    tech_posts=Post.tech.all()
    return render(request,'blog/tech.html',{'tech_posts':tech_posts})
def detailing(request,slug):
    template_name='single-post.html'
    post=get_object_or_404(Post,slug=slug)
    comments=post.commented.filter(active=True)
    new_comment=None
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.apost=post # apost is from Comment model
            new_comment.save()
    else:
        comment_form=CommentForm()
    dicti={'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form}
    
    return render(request,template_name,dicti)
     


    
