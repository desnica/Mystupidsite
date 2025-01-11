from django.shortcuts import render

# Create your views here.

def blog1(request):
    return render(request, 'blog1.html')
