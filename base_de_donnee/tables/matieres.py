import mysql.connector
from tkinter import messagebox


def create_table_matiere (us_m,pass_m,base_m):
    ma_base = mysql.connector.connect(
        host = "localhost",

        user = us_m,

        password = pass_m,

        database = base_m
    )
    mon_cursor = ma_base.cursor()
    try:
        mon_cursor.execute("CREATE TABLE matieres (id_matiere INT AUTO_INCREMENT NOT NULL PRIMARY KEY, code VARCHAR(50) NOT NULL UNIQUE, libelle VARCHAR(150) NOT NULL, coefficient INT NOT NULL)")
        return 1
    except:
        messagebox.showerror("Erreur","Impossible de creer la table")
