from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def authing(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog1')
        else:
            messages.success(request, ("Username or Password is incorrect. Try again."))
            return redirect('authing')   
    else:  
        return render(request, 'authing.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('blog1')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful."))
            return redirect('blog1')
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form':form,})