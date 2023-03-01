import os
import mysql.connector

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from ini import recuperation_bdname
from ini import NotesTablesManip
from ini import MatieresTablesManip
from ini import EtudiantsTablesManip
from ini import NotesTablesManip

def AjoutNotes():

    def Donnee():
        code = variable.get().strip("()")
        code_c = code.rstrip(",")
        code_d = code_c.strip("'")
        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        clee = code_d
        resultat = MatieresTablesManip.Recherche(clee, info_base)
        Id_matiere = resultat[0]

        try:
            Matricule = int(E1.get())

            Devoir = float(E2.get())

            Examen = float(E3.get())

            Projet = float(E4.get())

            info_base = recuperation_bdname.recuperation_de_toute_les_info()

            verif_mat = EtudiantsTablesManip.recherche_etudiant(Matricule, info_base)
            test_existance = isinstance(verif_mat, type(None))
            if Devoir > 20 or Examen > 20 or Projet > 20 :
                messagebox.showerror("Erreur","Une note ne  peut pas dépasser 20")
                return 0
            elif Devoir < 0 or Examen < 0 or Projet < 0:
                messagebox.showerror("Erreur","Une note ne  peut pas être inférieur à 0")
            elif test_existance:
                messagebox.showerror("Erreur","Ce matricule n'existe pas")
            else:
                return [Matricule,Id_matiere,Devoir,Examen,Projet,code_d]
        except:
            messagebox.showerror("Erreur","Les notes doivent être des réels")

    def AjoutDeNote():
        informations = Donnee()
        test = isinstance(informations, type(None))
        if test == True:
            return 0
        else:
            if informations == 0:
                return 0
            else:
                info_base = recuperation_bdname.recuperation_de_toute_les_info()
                resultat_insertion = NotesTablesManip.EnregistrementDesNotes(informations, info_base)
                if resultat_insertion == 1:
                    messagebox.showinfo("Success","Enregistrement de notes effectués")
                elif resultat_insertion == 0:
                    messagebox.showinfo("Echec","Enregistrements non effectué")
                elif resultat_insertion == 2:
                    messagebox.showinfo("Echec","Ce étudiant a déjà une note en "+informations[5])

    def menu():
        app.destroy()
        import menu
        menu.principale()

    app = Tk()
    app.geometry("2000x750+180+50")
    app.title("NOTES")

    lg= Canvas(app,width=1000,height=550)
    lg.place(x=0,y=10)
    Titre = Label(lg,text="ENREGISTREMENT DE NOTES",font=("arial",15,"bold"))
    Titre.place(x=0,y=15)



    L1 = Label(lg,text="Matricule",font=("arial",15,"bold"),fg="#FF0000")
    L1.place(x=80,y=70,width=200,height=40)

    L2 = Label(lg,text="Code Matière",font=("arial",15,"bold"),fg="#FF0000")
    L2.place(x=90,y=150,width=200,height=40)

    L3 = Label(lg,text="Devoir",font=("arial",15,"bold"),fg="#FF0000")
    L3.place(x=60,y=230,width=200,height=40)

    L4 = Label(lg,text="Examen",font=("arial",15,"bold"),fg="#FF0000")
    L4.place(x=65,y=310,width=200,height=40)

    L5= Label(lg,text="Projet",font=("arial",15,"bold"),fg="#FF0000")
    L5.place(x=55,y=390,width=200,height=40)

    """ LISTE DEROULANTE"""
    info_base = recuperation_bdname.recuperation_de_toute_les_info()
    liste = MatieresTablesManip.listematiere(info_base)
    
    variable = StringVar(app)
    variable.set(liste[0])

    opt = OptionMenu(app, variable, *liste)
    opt.config(width=26,font=("arial",12))
    opt.place(x=290,y=168)
    #variable.trace("w",code)

    """ENTRY"""
    E1 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E1.place(x=290,y=90)

    E2 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E2.place(x=290,y=248)

    E3 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E3.place(x=290,y=328)

    E4 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E4.place(x=290,y=408)

    b = Button(lg,text="AJOUTER",font=("arial",12),bg="blue",fg="#fff",command=AjoutDeNote)
    b.place(x=420,y=458,width=140)

    b = Button(lg,text="<<",font=("arial",12),bg="blue",fg="#fff",command=menu)
    b.place(x=260,y=458,width=140)



    #================================
    # AFFICHAGE DES ETUDIANTS
    #================================

    tree = ttk.Treeview(app,columns=(1,2,3,4) , show="headings")
    tree.place(x=700,y=80,width=600,height=300)

    tree.heading(1,text="Matricule")
    tree.heading(2,text="Nom")
    tree.heading(3,text="Prénom")
    tree.heading(4,text="Email")

    tree.column(1,width = 10)
    tree.column(2,width= 100)
    tree.column(3,width=100)
    tree.column(4,width = 100)


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



    app.mainloop()



def RMSNotes():

    def menu():
        app.destroy()
        import menu
        menu.principale()
    
    def Informations():
        code = variable.get().strip("()")
        code_c = code.rstrip(",")
        code_d = code_c.strip("'")

        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        clee = code_d

        Matricule = E1.get()

        resultat = MatieresTablesManip.Recherche(clee, info_base)
        Id_matiere = resultat[0]


        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        verif_mat = EtudiantsTablesManip.recherche_etudiant(Matricule, info_base)
        test_existance = isinstance(verif_mat, type(None))

        if Matricule == "":
            messagebox.showwarning("","Veuillez saisir le Matricule")
        elif test_existance == True:
            messagebox.showwarning("","Aucun étudiant ne correspond à ce matricule")
        else:
            return [int(Matricule),Id_matiere,code_d]

    def RechercheEtu():
        donne_saisie = Informations()
        test_variable = isinstance(donne_saisie, type(None))
        if test_variable == True:
            return 0
        else:
            AffichageListeEtButton(donne_saisie)
    
    def AffichageListeEtButton(donnee):

        def TableauDesInformations():
                try:
                    devoir_up = float(devoir_entry.get())
                    examen_up = float(examen_entry.get())
                    projet_up = float(projet_entry.get())

                    matricule_etu = donnee[0]
                    id_matiere = donnee[1]
                    code_matiere = donnee[2]
                    id_note = mon_tableau[0][8]
                    Tableau = [devoir_up,examen_up,projet_up,matricule_etu,id_matiere,id_note,code_matiere]
                    return Tableau
                except:
                    messagebox.showerror("","Une note est soite un entier soite un réel")
            
        def Modification():
            Tb = TableauDesInformations()
            modif = NotesTablesManip.ModificationDeNotes(Tb, info_base)
            if modif == 1:
                messagebox.showinfo("SUCCESS","Notes en "+Tb[6] +" modifiée avec success")
            elif modif == 0:
                messagebox.showerror("ECHEC","Modification Impossible")

        
        def Suppression():
            Tb = TableauDesInformations()
            delete = NotesTablesManip.SuppressionDeNotes(Tb, info_base)
            if delete == 1:
                messagebox.showinfo("SUCCESS","Notes en "+Tb[6] +" supprimés avec success")
            elif delete == 0:
                messagebox.showerror("Echec","Supression non effectuée")
        
        #================================
        # AFFICHAGE DES DONNEE DE LA BASE
        #================================

        tree = ttk.Treeview(app,columns=(1,2,3,4,5,6,7,8) , show="headings")
        tree.place(x=40,y=280,width=900,height=300)

        tree.heading(1,text="#")
        tree.heading(2,text="Nom")
        tree.heading(3,text="Prénom")
        tree.heading(4,text="Matière")
        tree.heading(5,text="Devoir")
        tree.heading(6,text="Examen")
        tree.heading(7,text="Projet")
        tree.heading(8,text="Moyenne")

        tree.column(1,width = 10)
        tree.column(2,width= 100)
        tree.column(3,width=100)
        tree.column(4,width = 100)
        tree.column(5,width = 100)
        tree.column(6,width = 100)
        tree.column(7,width = 100)
        tree.column(8,width = 100)


        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        mon_curseur = ma_base.cursor()
        mat = donnee[0]
        matiere = donnee[1]
        code_matiere = donnee[2]
        info = [mat,matiere]
        requete = "SELECT etudiants.matricule,nom,prenom,matieres.code,notes.devoir,notes.examen,notes.projet,(notes.projet + notes.devoir + notes.examen*2)/4 as Moyenne,obtenir.id_note FROM etudiants,obtenir,matieres,notes WHERE obtenir.matricule = etudiants.matricule AND obtenir.id_matiere = matieres.id_matiere AND obtenir.id_note = notes.id_note AND etudiants.matricule = %s AND obtenir.id_matiere = %s"
        mon_curseur.execute(requete,info)

        mon_tableau = mon_curseur.fetchall()
    
        if mon_tableau == []:
            messagebox.showinfo("","Ce Etudiant n'as aucune note en "+code_matiere)
        else:

            b1 = Button(lg,text="MODIFICATION",font=("arial",10),bg="blue",fg="#fff",command=Modification)
            b1.place(x=500,y=210,width=120)

            b2 = Button(lg,text="SUPPRESSION",font=("arial",10),bg="blue",fg="#fff",command=Suppression)
            b2.place(x=620,y=210,width=120)

            """ LABEL """
            devoir = Label(lg,text="Devoir",fg="#FF0000",font=("arial",12,"bold"))
            devoir.place(x=600,y=60)

            examen = Label(lg,text="Examen",fg="#FF0000",font=("arial",12,"bold"))
            examen.place(x=600,y=100)

            projet = Label(lg,text="Projet",fg="#FF0000",font=("arial",12,"bold"))
            projet.place(x=600,y=140)

            """ ENTRY """
            devoir_entry = Entry(app,width=20,relief=FLAT)
            devoir_entry.place(x=690,y=65)
            devoir_entry.insert(0, mon_tableau[0][4])

            examen_entry = Entry(app,width=20,relief=FLAT)
            examen_entry.place(x=690,y=105)
            examen_entry.insert(0, mon_tableau[0][5])

            projet_entry = Entry(app,width=20,relief=FLAT)
            projet_entry.place(x=690,y=145)
            projet_entry.insert(0,mon_tableau[0][6])


            for row in mon_tableau:
                tree.insert('', END,values = row)
            
            
        


    app = Tk()
    app.geometry("1050x700+180+40")
    app.title("MODIFICATION DE NOTES ")

    lg = Canvas(app,width=950)
    lg.place(x=0,y=5)
    Titre = Label(lg,text="RECHERCHE / MODIFICATION / SUPPRESSION",font=("arial",15,"bold"))
    Titre.place(x=5,y=10)

    L1 = Label(lg,text="MATRICULE",fg="#FF0000",font=("arial",12,"bold"))
    L1.place(x=120,y=70)

    L1 = Label(lg,text="CODE MATIÈRE",fg="#FF0000",font=("arial",12,"bold"))
    L1.place(x=120,y=135)

    
    E1 = Entry(app,width=30,font=("arial"),relief=FLAT)
    E1.place(x=270,y=65,height=30)


    """LISTE DEROULANT DES MATIERES"""
    info_base = recuperation_bdname.recuperation_de_toute_les_info()
    liste = MatieresTablesManip.listematiere(info_base)
    
    variable = StringVar(app)
    variable.set(liste[0])

    opt = OptionMenu(app, variable, *liste)
    opt.config(width=26,font=("arial",12))
    opt.place(x=270,y=135)


    precedent = Button(lg,text="<<",font=("arial",10),bg="blue",fg="#fff",command=menu)
    precedent.place(x=270,y=210,width=120)

    b = Button(lg,text="RECHERCHE",font=("arial",10),bg="blue",fg="#fff",command=RechercheEtu)
    b.place(x=380,y=210,width=120)

   

    app.mainloop()
