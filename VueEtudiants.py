import os
import mysql.connector

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from ini import recuperation_bdname
from ini import EtudiantsTablesManip

def InterfaceAjoutEtu():

    def TableauDonne():
        tree = ttk.Treeview(app,columns=(1,2,3,4,5) , show="headings")
        tree.place(x=100,y=380,width=900,height=300)

        tree.heading(1,text="Matricule")
        tree.heading(2,text="Nom")
        tree.heading(3,text="Prénom")
        tree.heading(4,text="Email")
        tree.heading(5,text="Sexe")

        tree.column(1,width = 10)
        tree.column(2,width= 100)
        tree.column(3,width=100)
        tree.column(4,width = 100)
        tree.column(5,width = 100)


        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        mon_curseur = ma_base.cursor()

        mon_curseur.execute("SELECT * FROM etudiants")
        
        for row in mon_curseur:
            tree.insert('', END,values = row)


    def recupe_input():
        nom = E1.get()
        prenom = E2.get()
        email = E3.get()
        sexe_e = sexe.get()
        if sexe_e == 1:
            sexe_final = "Homme"
        else:
            sexe_final = "Femme"
        
        if nom == "" or prenom == "" or email == "":
            messagebox.showwarning("Avertissement","Les champs ne doivent pas être vide")
        else:
            return [nom,prenom,email,sexe_final]

    def Envoi_de_donnee():
        donnee = recupe_input()

        """ RECUPERATION INFO DE LA BASE """
        info = recuperation_bdname.recuperation_de_toute_les_info()

        insertion = EtudiantsTablesManip.AjoutEtudiant(donnee, info)

        if insertion == 1:
            messagebox.showinfo("Reussie","Ajout effectuée😀")
            TableauDonne()
        else:
            messagebox.showerror("Erreur","Erreur lors de l'ajout des données")
    
    def menu():
        app.destroy()
        import menu
        menu.principale()
    
    app = Tk()
    app.geometry("950x550+180+50")
    app.title("Etudiants")

    lg = Canvas(app,width=1500,height=900)
    lg.place(x=0,y=5)
    Titre = Label(lg,text="ETUDIANTS",font=("arial",19,"bold"))
    Titre.place(x=10,y=10)

    """ LABEL """
    L1 = Label(lg,text="Nom",font=("arial",15,"bold"),fg="#FF0000")
    L1.place(x=80,y=70,width=200,height=40)


    L2 = Label(lg,text="Prénom",font=("arial",15,"bold"),fg="#FF0000")
    L2.place(x=90,y=150,width=200,height=40)

    L3 = Label(lg,text="Email",font=("arial",15,"bold"),fg="#FF0000")
    L3.place(x=80,y=230,width=200,height=40)

    """ ENTRY """

    E1 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E1.place(x=270,y=80,height=30)

    E2 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E2.place(x=270,y=160,height=30)

    E3 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E3.place(x=270,y=240,height=30)

    sexe = IntVar()
    sexe_h = Radiobutton(app,text="Homme",value=1,variable=sexe)
    sexe_h.place(x=300,y=290)
    sexe_f = Radiobutton(app,text="Femme",value=0,variable=sexe)
    sexe_f.place(x=400,y=290)

    b = Button(lg,text="AJOUTER",font=("arial",12),bg="blue",fg="#fff",command=Envoi_de_donnee)
    b.place(x=400,y=330,width=140)

    b2 = Button(lg,text="MENU",font=("arial",12),bg="blue",fg="#fff",command=menu)
    b2.place(x=220,y=330,width=140)




    #================================
    # AFFICHAGE DES DONNEE DE LA BASE
    #================================
    
    TableauDonne()
    

    app.mainloop()


def RMSEtudiant():

    """ RECHERCHE """
    def recherche():
        info_base = recuperation_bdname.recuperation_de_toute_les_info()

        matricule = cle()

        valeurs_retour = EtudiantsTablesManip.recherche_etudiant(matricule, info_base)
        
        return valeurs_retour
    
    """ RECUPERATION DE LA CLE"""
    def cle():
        mat = E1.get()
        if mat == "":
            messagebox.showerror("erreur","Veuillez entrez le matricule de l'etudiant")
        else:
            return mat


    """ AFFICHAGE DANS UN TABLEAU"""
    def affichage():
        Valeurs = recherche()
        test = isinstance(Valeurs, type(None))

        if test == True:
            messagebox.showerror("Erreur","Veuillez entrez un matricule correct | Celui entré n'existe pas")
        else:
            tree = ttk.Treeview(app,columns=(1,2,3,4,5) , height=10, show="headings")
            tree.place(x=100,y=260,width=900,height=300)


            tree.heading(1,text="MATRICULE")
            tree.heading(2,text="NOM")
            tree.heading(3,text="PRENOM")
            tree.heading(4,text="EMAIL")
            tree.heading(5,text="SEXE")

            tree.column(1,width = 5)
            tree.column(2,width= 100)
            tree.column(3,width=100)
            tree.column(4,width = 5)
            tree.column(5,width = 5)

            tree.insert('', END,values=Valeurs)

    """ SUPPRESSION """
    def suppression():
        matricule = cle()
        if matricule == "":
            messagebox.showinfo("Avertissement","Entrez un matricule")
        elif matricule:
            Valeurs = recherche()
            test = isinstance(Valeurs, type(None))
            if test:
                messagebox.showinfo("Avertissement","Ce matricule n'existe pas")
            else:
                information = recuperation_bdname.recuperation_de_toute_les_info()

                sup = EtudiantsTablesManip.SuppressionEtudiant(matricule, information)
                if sup == 1:
                    messagebox.showinfo("Reussite","Données de l'étudiant supprimé avec success")
                else:
                    messagebox.showerror("Echec","Impossible de supprimer les données de l'étudiant")

    

    """ MODIFICATION"""
    def modification():
        cle_de_recherche = cle()
        if cle_de_recherche == "":
            messagebox.showerror("Erreur","Veuillez d'abord renseigné le matricule")
        elif cle_de_recherche:
            InterfaceDeModification(cle_de_recherche)

    def InterfaceDeModification(cle_de_recherche):

        info_etudiant = recherche()
        test = isinstance(info_etudiant, type(None))

        if test == True:
            messagebox.showerror("Erreur","Le matricule que vous avez entrez ne correspond à aucun enregistrement")
        else:
            app.destroy()
            def updateEtudiant():
                matricule= info_etudiant[0]
                Nom = E1.get()
                Prenom = E2.get()
                Email = E3.get()
                if sexe.get() == 1:
                    sexe_finale = "Homme"
                else:
                    sexe_finale = "Femme"

                
                if Nom == "" or Prenom == "" or Email == "":
                    messagebox.showwarning("Warning","Attention veuillez renseigné les informations")
                else:
                    info_base = recuperation_bdname.recuperation_de_toute_les_info()
                    information = (Nom,Prenom,Email,matricule,sexe_finale)
                    modif = EtudiantsTablesManip.update(information, info_base)
                    if modif == 1:
                        messagebox.showinfo("Success","Modification effectué avec success")
                    elif modif == 0:
                        messagebox.showerror("Echec","Modification non effectuée")
                    

            def retour():
                update.destroy()
                RMSEtudiant()
            
            update = Tk()        
            update.geometry("950x550+180+50")
            update.title("Modification des données d'un étudiant")

            lg = Canvas(update,width=1500,height=900)
            lg.place(x=0,y=5)
            Titre = Label(lg,text="MODIFICATION "+info_etudiant[1],font=("arial",19,"bold"))
            Titre.place(x=10,y=10)

            L1 = Label(lg,text="Nom",font=("arial",15,"bold"),fg="#FF0000")
            L1.place(x=80,y=70,width=200,height=40)
                

            L2 = Label(lg,text="Prenom",font=("arial",15,"bold"),fg="#FF0000")
            L2.place(x=80,y=150,width=200,height=40)

            L3 = Label(lg,text="Email",font=("arial",15,"bold"),fg="#FF0000")
            L3.place(x=70,y=230,width=200,height=40)

            E1 = Entry(update,width=30,font=("arial"),relief=FLAT)
            E1.insert(0, info_etudiant[1])
            E1.place(x=270,y=80,height=30)

            E2 = Entry(update,width=30,font=("arial"),relief=FLAT)
            E2.insert(0,info_etudiant[2])
            E2.place(x=270,y=160,height=30)

            E3 = Entry(update,width=30,font=("arial"),relief=FLAT)
            E3.insert(0, info_etudiant[3])
            E3.place(x=270,y=240,height=30)

            sexe = IntVar()
            sexe_h = Radiobutton(update,text="Homme",value=1,variable=sexe)
            sexe_h.place(x=300,y=290)
            sexe_f = Radiobutton(update,text="Femme",value=0,variable=sexe)
            sexe_f.place(x=400,y=290)

            b = Button(lg,text="MODIFIER",font=("arial",12),bg="blue",fg="#fff",command=updateEtudiant)
            b.place(x=400,y=340,width=140)

            b2 = Button(lg,text="<<",font=("arial",12),bg="blue",fg="#fff",command=retour)
            b2.place(x=220,y=340,width=120)

            update.mainloop()

    """ FONCTION DE RETOUR EN ARRIÈRE"""
    def menu():
        app.destroy()
        import menu
        menu.principale()

        
    app = Tk()
    app.geometry("950x550+180+50")
    app.title("Operation sur la table ETUDIANT")

    lg = Canvas(app,width=1500,height=900)
    lg.place(x=0,y=5)
    Titre = Label(lg,text="Recherche / Modification / Suppression",font=("arial",19,"bold"))
    Titre.place(x=10,y=10)

    L1 = Label(lg,text="Matricule",font=("arial",15,"bold"),fg="#FF0000")
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
