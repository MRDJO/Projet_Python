import os
import mysql.connector
from tkinter import messagebox

def recuperation_du_nom_de_la_base():
    chemin_absolu = os.path.dirname(__file__)
    os.chdir(chemin_absolu)
    try:
        fichier_id = open("../base_info.txt","r")
        for ligne in fichier_id:
            element = ligne.split(":")
            cle = element[0]
            donnee = element[1]
            if cle == "Nom_base":
                return donnee
        
        fichier_id.close()
    except FileNotFoundError():
        messagebox.showerror("erreur fichier","Fichier de configuration inexistant")

def recuperation_user():
    chemin_absolu = os.path.dirname(__file__)
    os.chdir(chemin_absolu)
    try:
        fichier_id = open("../base_info.txt","r")
        for ligne in fichier_id:
            element = ligne.split(":")
            cle = element[0]
            donnee = element[1]
            if cle == "user":
                return donnee
        
        fichier_id.close()
    except FileNotFoundError():
        messagebox.showerror("erreur fichier","Fichier de configuration inexistant")


def recuperation_mdp():
    chemin_absolu = os.path.dirname(__file__)
    os.chdir(chemin_absolu)
    try:
        fichier_id = open("../base_info.txt","r")
        for ligne in fichier_id:
            element = ligne.split(":")
            cle = element[0]
            donnee = element[1]
            if cle == "mot_de_passe":
                return donnee
        
        fichier_id.close()
    except FileNotFoundError():
        messagebox.showerror("erreur fichier","Fichier de configuration inexistant")

def recuperation_de_toute_les_info():
    root = recuperation_user()
    name = recuperation_du_nom_de_la_base()
    mdp = recuperation_mdp()
    n_root = root.strip()
    n_name = name.strip()
    return [n_name,n_root,mdp]

