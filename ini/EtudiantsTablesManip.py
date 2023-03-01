import os
import mysql.connector
from tkinter import messagebox

def AjoutEtudiant(data,information):

    ma_base = mysql.connector.connect(
        host = "localhost",
        user = information[1],
        password = information[2],
        database = information[0]
    )
    nom = data[0]
    prenom = data[1]
    email = data[2]
    sexe = data[3]
    try:
        curseur = ma_base.cursor()

        requete = "INSERT INTO etudiants(nom,prenom,email,sexe) VALUES (%s,%s,%s,%s)"

        valeurs = [
            (nom,prenom,email,sexe)
        ]
        curseur.executemany(requete,valeurs)

        ma_base.commit()

        return 1
    except Exception as e:
        return 0


def SuppressionEtudiant(matricule,information):

    ma_base = mysql.connector.connect(
        host = "localhost",
        user = information[1],
        password = information[2],
        database = information[0]
    )

    try:
        curseur = ma_base.cursor()

        cle = [matricule]
        curseur.execute("DELETE FROM obtenir WHERE matricule = %s",cle)
        curseur.execute("DELETE FROM etudiants WHERE matricule = %s",cle)

        ma_base.commit()

        return 1
    except Exception as e:
        return 0

def recherche_etudiant(matricule,info_base):
    try:
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        curseur = ma_base.cursor()

        valeur = [matricule]
        curseur.execute('SELECT * FROM etudiants WHERE matricule = %s',valeur)

        for ligne in curseur:
            return ligne
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
        nom = information_a_modifier[0]
        prenom = information_a_modifier[1]
        email = information_a_modifier[2]
        matricule = information_a_modifier[3]
        sexe = information_a_modifier[4]
        req = 'UPDATE etudiants SET nom = %s,prenom = %s,email = %s,sexe = %s WHERE matricule = %s'
        valeur =[
            (nom,prenom,email,sexe,matricule)
        ]
        curseur.executemany(req,valeur)
        ma_base.commit()
        return 1
    except Exception as e:
        messagebox.showerror("",e)
        return 0

def releve(mat,info_base):
    try:
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        curseur = ma_base.cursor()

        list_des_donnes = dict()

        valeur = [mat,mat]
        curseur.execute('SELECT etudiants.nom,etudiants.prenom,matieres.code,matieres.coefficient,notes.devoir,notes.examen,notes.projet,(notes.examen*2 + notes.devoir + notes.projet)/4 as moyenne,((notes.examen*2 + notes.devoir + notes.projet)/4 * matieres.coefficient) As moyenne_coefficie,etudiants.sexe FROM etudiants,obtenir,notes,matieres WHERE obtenir.id_note = notes.id_note AND obtenir.id_matiere = matieres.id_matiere AND obtenir.matricule = %s AND etudiants.matricule = %s ',valeur)
        resultat1 = curseur.fetchall()

        list_des_donnes['generale'] = resultat1

        valeur1=[mat]
        curseur.execute('SELECT SUM(((notes.examen*2 + notes.devoir +notes.projet)/4) * matieres.coefficient) FROM obtenir,matieres,notes WHERE obtenir.id_note = notes.id_note AND obtenir.id_matiere = matieres.id_matiere AND obtenir.matricule = %s',valeur1)
        resultat_som_moyenne_coefficie = curseur.fetchall()

        list_des_donnes["moyenne_coefficie_total"] = resultat_som_moyenne_coefficie

        curseur.execute('SELECT SUM(matieres.coefficient) FROM obtenir,matieres WHERE  obtenir.id_matiere = matieres.id_matiere AND obtenir.matricule = %s',valeur1)
        resultat_som_coef = curseur.fetchall()

        list_des_donnes['somme_coef'] = resultat_som_coef[0][0]

        return list_des_donnes
    except Exception as e: 
        messagebox.showerror("Erreur",e)
        return 0