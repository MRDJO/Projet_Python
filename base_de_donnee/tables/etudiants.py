import mysql.connector
from tkinter import messagebox

def create_table_etudiant (ust,passt,baseo):
    ma_base = mysql.connector.connect(
        host = "localhost",

        user = ust,

        password = passt,

        database = baseo
    )
    mon_cursor = ma_base.cursor()
    try:
        mon_cursor.execute("CREATE TABLE etudiants(matricule INT AUTO_INCREMENT NOT NULL PRIMARY KEY,nom VARCHAR(150) NOT NULL,prenom VARCHAR(150) NOT NULL,email VARCHAR(150) NOT NULL,sexe varchar(10))")
        return 1
    except:
        messagebox.showerror("Erreur","Impossible de creer la table")
