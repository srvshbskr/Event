from django.shortcuts import render, redirect
from .forms import Userform,Loginform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def homePage(request):
    context = {}
    return render(request, 'app/homepage.html', context)


def signupPage(request):
    form = Userform()

    if request.method == 'POST':
        print(request.POST)
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'account created for user ')
            return redirect('login')

    context = {'form': form}
    return render(request, 'app/signup.html', context)


def loginPage(request):

    if request.method == "POST":
        form = Loginform(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"successfully logged in as %s"%username)
                return redirect("home")
            else:
                messages.error(request,'Incorrect username or password')
        else:
            messages.error(request,'Incorrect username or password')
    form = Loginform()
    context={"form":form}
    return render(request,"app/login.html", context)



def logoutPage(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")