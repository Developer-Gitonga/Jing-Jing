from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm,SearchForm, LoginForm
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect



def Home( request):
    return render(request, 'jingle/home.html')

def Cart( request):
    return render(request, 'jingle/cart.html')


def Login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    return render(request,'jingle/login.html',{'form':form})


def Signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = SignupForm()
    return render(request,'jingle/sign-up.html', {"form":form})