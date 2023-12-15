from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.views import View

# Create your views here.
class RegistrationFormView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'users/signup.html',{'form':form})

    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

