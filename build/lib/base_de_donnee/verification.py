import mysql.connector

from base_de_donnee.tables.etudiants import *
from base_de_donnee.tables.matieres import *
from base_de_donnee.tables.notes import *
from base_de_donnee.tables.obtenir import *

from tkinter import messagebox

def verif_exist_base_create_tables(us,passu,base_v):
    ma_base = mysql.connector.connect(
        host = "localhost",

        user = us,

        password = passu
    )

    test = 0

    mon_cursor = ma_base.cursor()

    mon_cursor.execute("SHOW DATABASES")

    base_reseach = base_v

    for base in mon_cursor:
        if base_reseach in base:
            test = 1
    if test == 1:
        messagebox.showinfo("Doublure","Cette base de donnée exist déjà 😶")
    else:
        mon_cursor.execute("CREATE DATABASE " + base_v)
        etu = create_table_etudiant(us, passu, base_v)
        mat = create_table_matiere(us, passu, base_v)
        note =create_table_note(us, passu, base_v)
        obtenir = create_table_obtenir(us, passu, base_v)
        if etu == 1 & mat == 1 & note == 1 & obtenir == 1:
            messagebox.showinfo("Success","Base de donnee et tables implementer avec success 😀")
            return 1
        else:
            messagebox.showerror("Erreur","Erreur lors de l'implementation de la base de donnee")
