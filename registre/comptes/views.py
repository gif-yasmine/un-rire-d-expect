from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import registreForm
from formulaires.models import Person, spirit, scolaire, professionnal
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
            messages.info(request, "Mots de passe ou Username incorrecte")
        
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

# vue de modification de parametre

# class VotreModeleUpdateView(UpdateView):
    
    # model = VotreModele
    # fields = ['champ1', 'champ2', ...]
    # template_name_suffix = '_update_form'
    # success_url = reverse_lazy('nom-de-la-page-de-success')

# déconnexion d'un compte
def deconnexion(request):
    logout(request)
    return redirect('connexion')

# page de connexion
def index(request):
    membres = Person.objects.all()
    context={
        'membres': membres
    }
    return render(request, 'pages/index.html', context)

# page profil
def profil(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/profil.html', context)