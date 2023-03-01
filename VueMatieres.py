import os
import mysql.connector

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from ini import recuperation_bdname
from ini import MatieresTablesManip

def InterfaceAjout():

    def TableauMatiere():
        tree = ttk.Treeview(app,columns=(1,2,3,4) , height=10, show="headings")
        tree.place(x=100,y=360,width=900,height=300)

        tree.heading(1,text="ID")
        tree.heading(2,text="Code matière")
        tree.heading(3,text="Nom")
        tree.heading(4,text="Coefficient")

        tree.column(1,width = 10)
        tree.column(2,width= 100)
        tree.column(3,width=100)
        tree.column(4,width = 10)

        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        mon_curseur = ma_base.cursor()

        mon_curseur.execute("SELECT * FROM matieres")
        
        for row in mon_curseur:
            tree.insert('', END,values = row)

    def DonneeEntree():
        code = E1.get()
        lib = E2.get()
        coef = E3.get()
        info = recuperation_bdname.recuperation_de_toute_les_info()
        result = MatieresTablesManip.Recherche(code, info)
        test = isinstance(result, type(None))
        if code == "" or lib == "" or coef == "":
            return 0
        elif test == False:
            messagebox.showerror("","Ce code existe déjà")
            return 0
        else:
            try:
                int(coef) 
                return [code,lib,coef]
            except:
                return 2

                
    def EnvoyerInfo():
        """ Donne entrée"""
        donnee = DonneeEntree()
        if donnee == 0:
            messagebox.showinfo("Echec","Veuillez entrez des données ")
        elif donnee == 2:
            messagebox.showinfo("Echec","Le coefficient doit être un entier")
        else:
            """ Info de connexion"""
            
            """ Envoi """
            info = recuperation_bdname.recuperation_de_toute_les_info()

            result = MatieresTablesManip.AjoutDeMatiere(donnee, info)

            if result == 1:
                messagebox.showinfo("Reussie","Ajout de matiere réussie 😀")
                TableauMatiere()
            else:
                messagebox.showinfo("Echec","Echec d'insertion 🤔")

    def menu():
        app.destroy()
        import menu
        menu.principale()


    app = Tk()
    app.geometry("900x550+180+50")
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


    Ie = Label(lg,text="Veuillez entrez les données",font=("arial",10,"bold"))
    Ie.place(x=150,y=20)

    """ ENTRY """


    E1 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E1.place(x=270,y=80,height=30)

    E2 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E2.place(x=270,y=160,height=30)

    E3 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E3.place(x=270,y=240,height=30)

    b = Button(lg,text="AJOUTER",font=("arial",12),bg="blue",fg="#fff",command=EnvoyerInfo)
    b.place(x=400,y=290,width=140)

    b2 = Button(lg,text="MENU",font=("arial",12),bg="blue",fg="#fff",command=menu)
    b2.place(x=220,y=290,width=140)

    #================================
    # AFFICHAGE DES DONNEE DE LA BASE
    #================================

    TableauMatiere()
    
    app.mainloop()



def RMSMatieres():

    def recherche():
        info_base = recuperation_bdname.recuperation_de_toute_les_info()

        cle_recherche = cle()

        resultat = MatieresTablesManip.Recherche(cle_recherche, info_base)

        return resultat

        
    
    def cle():
        mat = E1.get()
        if mat == "":
            messagebox.showerror("erreur","Veuillez entrez le code de la matiere")
        else:
            return mat

    def affichage():
        Valeurs = recherche()
        test = isinstance(Valeurs, type(None))

        if test == True:
            messagebox.showerror("Erreur","Veuillez entrez un code correct |  Celui entré n'existe pas")
        else:
            tree = ttk.Treeview(app,columns=(1,2,3,4) , height=10, show="headings")
            tree.place(x=100,y=260,width=900,height=300)


            tree.heading(1,text="ID")
            tree.heading(2,text="Code matière")
            tree.heading(3,text="Nom")
            tree.heading(4,text="Coefficient")

            tree.column(1,width = 5)
            tree.column(2,width= 100)
            tree.column(3,width=100)
            tree.column(4,width = 5)
            tree.insert('', END,values=Valeurs)
 

    def suppression():
        valeurs_r = recherche()
        matiere = cle()
        info = [valeurs_r[0],matiere]
        information = recuperation_bdname.recuperation_de_toute_les_info()

        sup = MatieresTablesManip.SuppressionDeMatiere(info, information)
        if sup == 1:
            messagebox.showinfo("Reussite","Matiere supprimée avec success")
        else:
            messagebox.showerror("Echec","Impossible de supprimer la matiere")
    
    def Interfaceupdate(cle_de_recherche):
    
        info_matiere = recherche()
        test = isinstance(info_matiere, type(None))

        if test == True:
            messagebox.showerror("Erreur","Le code que vous avez entrez ne correspond à aucun enregistrement")
        else:
            app.destroy()
            def updatematiere():
                id_matiere = info_matiere[0]
                code = E1.get()
                libelle = E2.get()
                coef = E3.get()
                if code == "" or libelle == "" or coef == "":
                    messagebox.showwarning("Warning","Attention veuillez renseigné les informations")
                else:
                    try:
                        int(coef)
                        info_base = recuperation_bdname.recuperation_de_toute_les_info()
                        information = (code,libelle,coef,id_matiere)
                        modif = MatieresTablesManip.update(information, info_base)
                        if modif == 1:
                            messagebox.showinfo("Success","Modification effectué avec success")
                        elif modif == 0:
                            messagebox.showerror("Echec","Modification non effectuée")
                    except:
                        messagebox.showerror("Erreur","Erreur d'insertion")

            def retour():
                update.destroy()
                RMSMatieres()
            
            update = Tk()        
            update.geometry("950x550+180+50")
            update.title("Modification d'une matiere")

            lg = Canvas(update,width=1500,height=900)
            lg.place(x=0,y=5)
            Titre = Label(lg,text="MODIFICATION DE '"+cle_de_recherche+"'",font=("arial",19,"bold"))
            Titre.place(x=10,y=10)

            L1 = Label(lg,text="Code Matiere",font=("arial",15,"bold"),fg="#FF0000")
            L1.place(x=80,y=70,width=200,height=40)
                

            L2 = Label(lg,text="Nom Matiere",font=("arial",15,"bold"),fg="#FF0000")
            L2.place(x=80,y=150,width=200,height=40)

            L3 = Label(lg,text="Coefficient",font=("arial",15,"bold"),fg="#FF0000")
            L3.place(x=70,y=230,width=200,height=40)

            E1 = Entry(update,width=30,font=("arial"),relief=FLAT)
            E1.insert(0, info_matiere[1])
            E1.place(x=270,y=80,height=30)

            E2 = Entry(update,width=30,font=("arial"),relief=FLAT)
            E2.insert(0,info_matiere[2])
            E2.place(x=270,y=160,height=30)

            E3 = Entry(update,width=30,font=("arial"),relief=FLAT)
            E3.insert(0, info_matiere[3])
            E3.place(x=270,y=240,height=30)

            b = Button(lg,text="MODIFIER",font=("arial",12),bg="blue",fg="#fff",command=updatematiere)
            b.place(x=400,y=290,width=140)

            b2 = Button(lg,text="<<",font=("arial",12),bg="blue",fg="#fff",command=retour)
            b2.place(x=220,y=290,width=120)

            update.mainloop()

    def modification():

        cle_de_recherche = cle()
        if cle_de_recherche == "":
            messagebox.showerror("Erreur","Veuillez d'abord renseigné le code de la matiere")
        elif cle_de_recherche:
            Interfaceupdate(cle_de_recherche)
    
        
    def menu():
        app.destroy()
        import menu
        menu.principale()

    app = Tk()
    app.geometry("950x550+180+50")
    app.title("Operation sur la table matiere")

    lg = Canvas(app,width=1500,height=900)
    lg.place(x=0,y=5)
    Titre = Label(lg,text="Recherche / Modification / Suppression",font=("arial",19,"bold"))
    Titre.place(x=10,y=10)

    L1 = Label(lg,text="Code Matiere",font=("arial",15,"bold"),fg="#FF0000")
    L1.place(x=40,y=70,width=200,height=40)

    E1 = Entry(app,width=50,font=("arial"),relief=FLAT)
    E1.place(x=270,y=80,height=30)

    b1 = Button(lg,text="RECHERCHE",font=("arial",12),bg="blue",fg="#fff",command=affichage)
    b1.place(x=270,y=130,width=130)

    b2 = Button(lg,text="MODIFICATION",font=("arial",12),bg="blue",fg="#fff",command=modification)
    b2.place(x=420,y=130,width=130)
    

    b3 = Button(lg,text="SUPPRESSION",font=("arial",12),bg="blue",fg="#fff",command=suppression)
    b3.place(x=570,y=130,width=130)

    b4 = Button(lg,text="MENU",font=("arial",12),bg="blue",fg="#fff",command=menu)
    b4.place(x=720,y=130,width=130)


    app.mainloop()


