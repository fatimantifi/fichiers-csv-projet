from csv import *
import os
from csv import DictReader

with open ('tableauexcel.csv',"r", encoding ='utf-8-sig') as file:
    reader = csv.reader(File, delimiter=';')
    for line in reader:
        link.append(line)

def recup_liens(sous_listes):
    a=str(sous_listes)
    L=[]
    k=a.split(';')
    for elt in k:
        site.append(elt)
        L.append(elt)

#def ajustement des rangées
#definir colonnes
