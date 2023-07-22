from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    numero = models.CharField(max_length=14)
    date = models.DateField(null=True, default=None)
    location = models.CharField(max_length=100, blank=True)
    commune = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} {self.prenoms} {self.email} {self.numero} {self.date} {self.location} {self.commune} {self.status} {self.genre}"
    
class spirit(models.Model):
    person = models.ForeignKey(Person,null=True, on_delete=models.CASCADE)
    baptism_water = models.CharField(max_length=3, default=None)
    date = models.DateField(null=True, blank=True)
    baptism_spirit = models.CharField(max_length=3, default=None)
    community = models.CharField(max_length=16,null=True, blank=True, default=None)
    jeunesse = models.CharField(max_length=8,null=True, blank=True, default=None)
    
class scolaire(models.Model):
    person = models.ForeignKey(spirit,null=True,default=None, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=21,null=True, blank=True)
    diplomes = models.CharField(max_length=12,null=True, blank=False)
    series = models.CharField(max_length=12,null=True, blank=True)
    filieres = models.CharField(max_length=36,null=True, blank=True)
    
class professionnal(models.Model):
    person = models.ForeignKey(scolaire,null=True, on_delete=models.CASCADE)
    domaine = models.CharField(max_length=21,null=True, blank=True)
    working = models.CharField(max_length=3,null=True, blank=True)
    metier= models.CharField(max_length=80,null=True, blank=True)
    description = models.TextField(blank=True, default=None)
    cv = models.FileField(upload_to='PDF/CV/', null=True)
    image_de_profil = models.ImageField(upload_to='Pictures/profil', null=True)
    
