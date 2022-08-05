from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from my_auth.forms import CustomAuthForm, CustomCreateForm
# Create your views here.
def my_register(request):
    form = CustomCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("my_auth.login")
    return render(request,"my_auth/register.html",{"form" : form})


def my_login(request):
    if request.method == "POST":
        form = CustomAuthForm(request,request.POST)
    else:
        form = CustomAuthForm()
    attempt = False
    if form.is_valid():
        user_obj = form.get_user()
        authenticate(request)
        login(request,user_obj)
        return redirect("myapp.home")
    else:
        if form.is_bound:
            print("hello")
            attempt = True
    return render(request,"my_auth/login.html",{"form" : CustomAuthForm(),"attempt" : attempt})

@login_required
def my_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("my_auth.login")
    else:
        return redirect("myapp.home")