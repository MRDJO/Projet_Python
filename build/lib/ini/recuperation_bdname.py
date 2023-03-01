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
