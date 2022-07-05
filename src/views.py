from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm,SearchForm, LoginForm
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Home( request):
    return render(request, 'jingle/home.html')

def Cart( request):
    return render(request, 'jingle/cart.html')


def Login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        print("logged in STEP 1 ")
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

@login_required
def logout(request):
    # logout(request)
    return HttpResponse("logged out")


def Signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = SignupForm()
    return render(request,'jingle/sign-up.html', {"form":form})


# # class ProfileView(LoginRequiredMixin, View):
# #     login_url = '/login/'
# #     """this class view is used to render the profile page and execute user profile updates."""

#     def Profile(self, request):
#         user = request.user
        
#         profile = get_object_or_404(UserProfile, user=user)
#         context = {
#             'title': 'Profile',
#             'user_data': user,
#             'profile_data': profile,
           
#         }
#         return render(request, 'jingle/profile.html')


# # profile design
# # @login_required
# def edit_profile(request, pk):
#     user = User.objects.get(pk=pk)

#     # prepolate the form with the user's data
#     user_form = UserForm(instance=user)

#     ProfileInlineFormSet = inlineformset_factory(
#         User, UserProfile, fields=('bio', 'phone', 'picture'), extra=0)
#     formset = ProfileInlineFormSet(instance=user)

#     if request.user.is_authenticated and request.user.id == user.id:
#         if request.method == 'POST':
#             user_form = UserForm(
#                 request.POST, request.FILES, instance=user)
#             formset = ProfileInlineFormSet(
#                 request.POST, request.FILES, instance=user)

#             if user_form.is_valid():
#                 created_user = user_form.save(commit=False)
#                 formset = ProfileInlineFormSet(
#                     request.POST, request.FILES, instance=created_user)
#                 if formset.is_valid():
#                     created_user.save()
#                     formset.save()
#                     return HttpResponseRedirect('/profile/')

#         return render(request, 'jingke/edit_profile.html', {
#             "pk": pk,
#             "user_form": user_form,
#             "formset": formset,
#         })
#     else:
#         raise PermissionDenied