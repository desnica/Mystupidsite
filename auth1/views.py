from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
