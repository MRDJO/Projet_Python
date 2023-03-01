import mysql.connector
from tkinter import messagebox


def create_table_obtenir (ust,passt,baseo):
    ma_base = mysql.connector.connect(
        host = "localhost",

        user = ust,

        password = passt,

        database = baseo
    )
    mon_cursor = ma_base.cursor()
    try:
        mon_cursor.execute("CREATE TABLE obtenir(id_note INT ,matricule INT ,id_matiere INT,CONSTRAINT FK_obtenirmatieres FOREIGN KEY(id_matiere) REFERENCES matieres(id_matiere),CONSTRAINT FK_obtenirnotes FOREIGN KEY(id_note) REFERENCES notes(id_note),CONSTRAINT FK_obteniretudiants FOREIGN KEY(matricule) REFERENCES etudiants(matricule),PRIMARY KEY(id_note,matricule,id_matiere))")
        return 1
    except:
        messagebox.showerror("Erreur","Impossible de creer la table")
