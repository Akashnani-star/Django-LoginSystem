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
    else:
        return render(request,"my_auth/register.html",{"form" : form})


def my_login(request):
    form = CustomAuthForm(request,request.POST)
    if form.is_valid():
        user_obj = form.get_user()
        authenticate(request)
        login(request,user_obj)
        return redirect("myapp.home")
    else:
        return render(request,"my_auth/login.html",{"form" : CustomAuthForm()})

@login_required
def my_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("my_auth.login")
    else:
        return redirect("myapp.home")