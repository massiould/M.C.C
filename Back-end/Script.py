from Accounts.models import Lawyer_identification
from datetime import datetime
import csv
from django.db.models import Q



def importer_donnees_csv(chemin_du_fichier):

    with open(chemin_du_fichier, 'r', encoding='ISO-8859-1') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv, delimiter=';')
        for ligne in lecteur_csv:
            Lawyer_identification.objects.create(
                barreau=ligne.get('NomBarreau',None),
                name=ligne.get('avNom',None),
                surname = ligne.get('avPrenom',None),
                raisonsociale=ligne.get('cbRaisonSociale',None),
                siren=ligne.get('cbSiretSiren',None),
                adresse=ligne.get('cbAdresse1',None),
                adresse_continue=ligne.get('cbAdresse2',None),
                codepostale=ligne.get('cbCp',None),
                ville=ligne.get('cbVille',None), 
                specialite=ligne.get('spLibelle1',"None") + ', ' + ligne.get('spLibelle2',"None") + ', ' + ligne.get('spLibelle3',"None"),
                dateserment = ligne.get('acDateSerment', None),
                langue=ligne.get('avLang',None)
            )

chemin_du_fichier_csv = '/home/mouldrabah/Documents/Dev/Avocat/check_list.csv'
#importer_donnees_csv(chemin_du_fichier_csv)
def supprimer_entrees_vide():
    entrees_vide = Lawyer_identification.objects.all()
    for entree in entrees_vide:
        entree.delete()

#supprimer_entrees_vide()