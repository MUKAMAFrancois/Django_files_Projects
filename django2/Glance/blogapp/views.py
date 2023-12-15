from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post
from django.views.generic.edit import CreateView,UpdateView

# Create your views here.
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password2==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                User.objects.create_user(username=username,email=email,password=password1).save();
                return redirect('login')
        else:
            messages.info(request,"Password Mismatch")
            return redirect('register')
    else:
        return render(request,'blogapp/signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Invalid credintials")
            return redirect('login')
    else:
        return render(request,'blogapp/just_login.html')

# list of all posts
def index(request):
    posts=Post.objects.all()
    return render(request,'blogapp/index.html',{'posts':posts})
# details upon clicking the head title

def readfull(request,pk):
    post_by_id=Post.objects.get(id=pk)
    return render(request,'blogapp/full_text.html',{'post_by_id':post_by_id})

def logout(request):
    return redirect('blogapp:login')