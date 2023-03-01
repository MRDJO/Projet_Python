import os

from tkinter import *
from tkinter import messagebox

from ini import recuperation_bdname
from ini import MatieresTablesManip

def InterfaceAjout():
    def DonneeEntree():
        code = E1.get()
        lib = E2.get()
        coef = E3.get()
        return [code,lib,coef]

    def EnvoyerInfo():
        """ Donne entrée"""
        donnee = DonneeEntree()

        """ Info de connexion"""
        root = recuperation_bdname.recuperation_user()
        name = recuperation_bdname.recuperation_du_nom_de_la_base()
        mdp = recuperation_bdname.recuperation_mdp()

        """ Envoi """
        info = [name,root,mdp]

        result = MatieresTablesManip.AjoutDeMatiere(donnee, info)

        if result == 1:
            print("En tout cas")

    app = Tk()
    app.geometry("1000x650+180+50")
    app.title("Ajout de Matiere")
    
    lg = Canvas(app,width=1500,height=900)
    lg.place(x=0,y=5)
    Titre = Label(lg,text="Matiere",font=("arial",19,"bold"))
    Titre.place(x=10,y=10)

    """ LABEL """
    L1 = Label(lg,text="Code Matiere",font=("arial",15,"bold"),fg="#FF0000")
    L1.place(x=80,y=70,width=200,height=40)


    L2 = Label(lg,text="Nom Matiere",font=("arial",15,"bold"),fg="#FF0000")
    L2.place(x=80,y=150,width=200,height=40)

    L3 = Label(lg,text="Coefficient",font=("arial",15,"bold"),fg="#FF0000")
    L3.place(x=70,y=230,width=200,height=40)

    """ ENTRY """


    E1 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E1.place(x=270,y=80,height=30)

    E2 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E2.place(x=270,y=160,height=30)

    E3 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E3.place(x=270,y=240,height=30)

    b = Button(lg,text="AJOUTER",font=("arial",12),bg="blue",fg="#fff",command=EnvoyerInfo)
    b.place(x=400,y=290,width=140)

    app.mainloop()

root = recuperation_bdname.recuperation_user()

print(root)