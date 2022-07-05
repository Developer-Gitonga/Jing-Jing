from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views import View



def Home( request):
    return render(request, 'jingle/home.html')

def Cart( request):
    return render(request, 'jingle/cart.html')

# def Login( request):
#     return render(request, 'jingle/login.html')

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


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()
    return render(request,'jingle/sign-up.html', {"form":form})