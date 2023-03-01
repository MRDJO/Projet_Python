import mysql.connector
from tkinter import messagebox



def create_table_note (ust,passt,baseo):
    ma_base = mysql.connector.connect(
        host = "localhost",

        user = ust,

        password = passt,

        database = baseo
    )
    mon_cursor = ma_base.cursor()
    try:
        mon_cursor.execute("CREATE TABLE notes(id_note INT AUTO_INCREMENT NOT NULL PRIMARY KEY,devoir FLOAT DEFAULT 0 ,examen FLOAT DEFAULT 0,projet FLOAT DEFAULT 0) ")
        return 1
    except:
        messagebox.showerror("Erreur","Impossible de creer la table")

