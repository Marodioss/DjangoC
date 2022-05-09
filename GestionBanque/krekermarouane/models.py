
from http import client
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.



   
class Client (models.Model):
    code = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    dateOperation = models.DateField()
    montant = models.FloatField()
    type = models.CharField(max_length=40)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
class Compte(models.Model):
    numero = models.CharField(max_length=40)
    dateCreation = models.DateField()
    solde = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operation = models.OneToOneField(Operation,on_delete=models.CASCADE)
    
    
    

    
    
    
    

