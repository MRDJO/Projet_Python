from tkinter import *
from tkinter import ttk

from VueMatieres import *
from VueEtudiants import *
from VueNotes import *
from VueReleves import *


from ini import NotesTablesManip

from ini import recuperation_bdname 

def principale():
    def etuajout():
        app.destroy()
        InterfaceAjoutEtu()
    def etuup():
        app.destroy()
        RMSEtudiant()

    def matajout():
        app.destroy()
        InterfaceAjout()

    def upmat():
        app.destroy()
        RMSMatieres()

    def notess():
        app.destroy()
        AjoutNotes()
    
    def upnotes():
        app.destroy()
        RMSNotes()

    def releve():
        app.destroy()
        Impression()

    def CountMatiereAndAffichage():
        info_base = recuperation_bdname.recuperation_de_toute_les_info()
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        curseur = ma_base.cursor()
        curseur.execute("SELECT COUNT(*) FROM matieres")
        nombre = curseur.fetchone()[0]
        tree = ttk.Treeview(app,columns=(1,2,3,4,5,6,7),show="headings")
        tree.place(x=10,y=65,width=1200,height=700)
            
        tree.heading(1,text="NOM")
        tree.heading(2,text="PRENOM")
        tree.heading(3,text="Matiere")
        tree.heading(4,text="Devoir")
        tree.heading(5,text="Examen")
        tree.heading(6,text="Projet")
        tree.heading(7,text="Moyenne")

        tree.column(1,width=75)
        tree.column(2,width=75)
        tree.column(3,width=75)
        tree.column(4,width=75)
        tree.column(5,width=75)
        tree.column(6,width=75)
        tree.column(7,width=75)

        if nombre != 0 :
            MoyenneEtu = NotesTablesManip.Moyennes(info_base)
            for row in MoyenneEtu:
                tree.insert('', END,values = row)
        
            
        
    
    app = Tk()
    app.geometry("2000x550+180+50")
    app.title("APPLICATION DE GESTION DES NOTES -- MENU PRINCIPALE")


    mainmenu = Menu(app)


    first_menu = Menu(mainmenu,tearoff=0)
    """ SOUS MENU  ETUDIANTS"""
    first_menu.add_command(label="AJOUT",command=etuajout)
    first_menu.add_command(label="RECHERCHE / MODIFICATION / SUPPRESSION",command=etuup)


    second_menu = Menu(mainmenu,tearoff=0)
    """ SOUS MENU MATIERES"""
    second_menu.add_command(label="AJOUT",command=matajout)
    second_menu.add_command(label="RECHERCHE / MODIFICATION / SUPPRESSION",command=upmat)


    third_menu = Menu(mainmenu,tearoff=0)
    """ SOUS MENU NOTES"""
    third_menu.add_command(label="AJOUT",command=notess)
    third_menu.add_command(label="RECHERCHE / MODIFICATION / SUPPRESSION",command=upnotes)

    fourmenu = Menu(mainmenu,tearoff=0)
    fourmenu.add_command(label="RELEVE",command=releve)

    mainmenu.add_cascade(label="Gestions des etudiants",menu=first_menu)
    mainmenu.add_cascade(label="Gestions des matieres",menu=second_menu)
    mainmenu.add_cascade(label="Gestions des notes",menu=third_menu)
    mainmenu.add_cascade(label="Recapitulatif",menu=fourmenu)


    lg= Canvas(app,width=1500,height=550)
    lg.place(x=0,y=10)
    Titre = Label(lg,text="NOTES ET MOYENNES PAR ÉLÈVE",font=("arial",15,"bold"))
    Titre.place(x=10,y=15)

    CountMatiereAndAffichage()

    app.config(menu=mainmenu)
    app.mainloop()
