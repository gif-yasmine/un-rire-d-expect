from django.shortcuts import render

# Create your views here.

# vue d'enregistrement du formulaire d'identification
def identification(request):
    return render(request, 'pages/identification.html')

# vue d'enregistrement du formulaire spirituel
def spirituel(request):
    return render(request, 'pages/spirituel.html')

# vue d'enregistrement du formulaire d'education
def education(request):
    return render(request, 'pages/education.html')

# vue d'enregistrement du formulaire de profession
def professionel(request):
    return render(request, 'pages/professionnel.html')