from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import registreForm
# Create your views here.

# formulaire de connexion
def connexion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Mots de passe ou Username incorrecte")
        
    return render(request,'connexion.html')

# formulaire de création de compte
def registre(request):
    form = registreForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            redirect('connexion')
        else:
            messages.info(request, "Mots de passe ou Username incorrecte")
    
    form = registreForm()
    context = {
        'form': form
    }         
    return render(request, 'registre.html',context)

# déconnexion d'un compte
def deconnexion(request):
    logout(request)
    return render(request,'connexion.html')

# page de connexion
def index(request):
    return render(request, 'pages/index.html')

# page profil
def profil(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/profil.html', context)