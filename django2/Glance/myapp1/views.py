from django.shortcuts import (
    render,
    redirect, # new
)
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Services
from django.views.generic import(
    ListView
)

# Create your views here.

class Display(ListView):
    model=Services
    template_name='from_out/index.html'
    context_object_name='all_services'

# we can do the same by FBV

# def display(request):
#   all_services=Services.objects.all()
#    return render(request,'from_out/index.html',{'all_services':all_services})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists") # we need to show this message on register form by for loop
                return redirect('register') # user returns to that form again
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email,password=password1)
                user.save();
                return redirect('login') # we need to create this 'login' url
        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')
    else:
        return render(request,'myapp1/register.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credintials are Invalid")
            return redirect('login')
    else:
        return render(request, 'myapp1/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')



def detailView(request,pk):
    return render(request,'myapp1/detail.html',{'pk':pk})

def listing(request):
    posts=["John Dalton","ALan Killer","989","Alleluah Joseph"]
    return render(request,'myapp1/listing.html',{'posts':posts})

