from django.db import models
from django.utils.translation import gettext_lazy as _



class Lawyer_identification(models.Model):
    siren = models.CharField(max_length=100, blank=True, null=True)
    barreau = models.CharField(max_length=100, blank=True, null=True)
    name =  models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    raisonsociale = models.CharField(max_length=100, blank=True, null=True)
    adresse =  models.CharField(max_length=100, blank=True, null=True)
    adresse_continue =  models.CharField(max_length=100, blank=True, null=True)
    codepostale = models.CharField(max_length=10, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    specialite = models.CharField(max_length=200, blank=True, null=True)
    dateserment = models.CharField(max_length=200, blank=True, null=True)
    langue = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name 

    




    
    

