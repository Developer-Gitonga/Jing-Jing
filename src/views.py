from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views import View



def Home( request):
    return render(request, 'jingle/home.html')

def Cart( request):
    return render(request, 'jingle/cart.html')

def Login( request):
    return render(request, 'jingle/login.html')