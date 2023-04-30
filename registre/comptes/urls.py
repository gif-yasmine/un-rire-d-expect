from django.urls import path
from . import views

# app_name= "comptes"

urlpatterns = {
    path('connexion',views.connexion ,name="connexion"),
    path('registre',views.registre, name="registre"),
    path('index',views.index, name='index'),
    path('deconnexion',views.deconnexion,name="deconnexion"),
    path('profil', views.profil, name="profil"),
}