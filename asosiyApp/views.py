from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('parol')
        )
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/bulimlar/')
    return render(request, 'home.html')

def bulimlar(request):
    if request.user.is_authenticated:
        return render(request, 'bulimlar.html')
    return redirect('/')

def client_update(request):
    return render(request, 'client_update.html')

def clients(request):
    return render(request, 'clients.html')

def product_update(request):
    return render(request, 'product_update.html')

def products(request):
    return render(request, 'products.html')

def stats(request):
    return render(request, 'stats.html')

def logout_view(request):
    logout(request)
    return redirect('/')

