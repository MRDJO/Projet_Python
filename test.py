import os
from ini import recuperation_bdname

from tkinter import *
import mysql.connector
from tkinter import messagebox
"""
if base_creer == 1:
    root = Tk()

    a = Toplevel(root, bg='red')
    b = Toplevel(root, bg='blue')

    root.mainloop()
else:
    messagebox.showinfo("Info","Veuillez configurer la base de donnee")
try :
    
except:
    print("tres bien")
"""
ma_base = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "adminroot",
    database = "TP_PYTHON"
)
curseur = ma_base.cursor()
curseur.execute("SELECT * FROM etudiants")
tt = curseur.fetchall()
