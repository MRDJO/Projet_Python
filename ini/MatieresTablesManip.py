import os
import mysql.connector
from tkinter import messagebox

def AjoutDeMatiere(data,information):

    ma_base = mysql.connector.connect(
        host = "localhost",
        user = information[1],
        password = information[2],
        database = information[0]
    )
    code = data[0]
    lib = data[1]
    coef = data[2]
    coef = int(coef)
    try:
        curseur = ma_base.cursor()
        
        requete = "INSERT INTO matieres(code,libelle,coefficient) VALUES (%s,%s,%s)"

        valeurs = [
            (code,lib,coef)
        ]
        curseur.executemany(requete,valeurs)

        ma_base.commit()

        return 1
    except:
        return 0


def SuppressionDeMatiere(code,information):

    ma_base = mysql.connector.connect(
        host = "localhost",
        user = information[1],
        password = information[2],
        database = information[0]
    )

    try:
        curseur = ma_base.cursor()

        codematiere = [code[1]]
        idmat =[code[0]]
        curseur.execute("DELETE FROM obtenir WHERE id_matiere = %s",idmat)
        curseur.execute("DELETE FROM matieres WHERE code = %s",codematiere)

        ma_base.commit()

        return 1
    except Exception as e:
        return 0


def Recherche(clee,info_base):
    try:
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        curseur = ma_base.cursor()

        codemat = clee

        valeur = [codemat]
        curseur.execute('SELECT * FROM matieres WHERE code = %s',valeur)

        for ligne in curseur:
            return ligne
    except Exception as e: 
        messagebox.showerror("Erreur",e)
        return 0

def listematiere(info_base):
    try:
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        curseur = ma_base.cursor()

        curseur.execute('SELECT code FROM matieres ')

        informations = curseur.fetchall()

        return informations
    except Exception as e: 
        messagebox.showerror("Erreur",e)
        return 0



def update(information_a_modifier,info_base):
    try:
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
            )
        curseur = ma_base.cursor()
        code = information_a_modifier[0]
        libelle = information_a_modifier[1]
        coef = information_a_modifier[2]
        matiere = information_a_modifier[3]
        req = 'UPDATE matieres SET code = %s,libelle = %s,coefficient = %s WHERE id_matiere = %s'
        valeur =[
            (code,libelle,coef,matiere)
        ]
        curseur.executemany(req,valeur)
        ma_base.commit()
        return 1
    except Exception as e:
        messagebox.showerror("",e)
        return 0