from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    return render(request, 'account/signup.html')


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'account/dashboard.html')
