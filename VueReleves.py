import os
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from ini import recuperation_bdname
from ini import EtudiantsTablesManip

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch

def Impression():
    def menu():
        app.destroy()
        import menu
        menu.principale()
    

    def recupMatricule():
        try:
            matricule = int(E1.get())

            info_base = recuperation_bdname.recuperation_de_toute_les_info()

            verif_mat = EtudiantsTablesManip.recherche_etudiant(matricule, info_base)
            test_existance = isinstance(verif_mat, type(None))
            if test_existance:
                messagebox.showerror("","Le matricule que vous avez entrez ne correspond à aucun étudiant")
            else:
                TableauInformationEtudiants = EtudiantsTablesManip.releve(matricule, info_base)
                moy = isinstance(TableauInformationEtudiants["moyenne_coefficie_total"], type(None))
                coef = isinstance(TableauInformationEtudiants["somme_coef"], type(None))
                if TableauInformationEtudiants['generale'] == "" or moy or coef :
                    messagebox.showinfo("","Cet Etudiant n'as encore aucune note")
                else:
                    generation_pdf(TableauInformationEtudiants)
        except:
            messagebox.showerror("","Veuillez entre un matricule correct")


    app = Tk()
    app.geometry("2000x900")
    app.title("Releve par eleve")

    Titre = Label(app,text="GENERATION DU RELEVE PAR ELEVE",font=("Helvatica",10,"bold"))
    Titre.place(x=0,y=10)

    L1 = Label(app,text="Veuillez entrez le matricule de l'élève : ",font=("arial",15,"bold"),fg="red")
    L1.place(x=20,y=100)

    E1 = Entry(app,relief=FLAT)
    E1.place(x=400,y=100,height=30,width=250)

    B = Button(app,text="Générer",fg="#fff",bg="blue",font=("arial",13,"bold"),command=recupMatricule)
    B.place(x=500,y=160,width=150)

    B = Button(app,text="<<",fg="#fff",bg="blue",font=("arial",13,"bold"),command=menu)
    B.place(x=300,y=160,width=150)

    #=====================
    #==LISTE DES ETUDIANTS
    #=====================
    tree = ttk.Treeview(app,columns=(1,2,3,4) , show="headings")
    tree.place(x=100,y=250,width=900,height=300)

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

def generation_pdf(donnees):
    try:
        donnee_generaux = donnees['generale']
        nom = donnee_generaux[0][0]
        prenom = donnee_generaux[0][1]
        nomPrenom = nom+prenom
        sexe = donnee_generaux[0][9]
        total_coef = donnees['somme_coef']
        moyenne_total = donnees["moyenne_coefficie_total"][0][0]
        moyenne_generale = float(moyenne_total) / float(total_coef)
        

        chemin_absolu = os.path.dirname(__file__)
        os.chdir(chemin_absolu)


        fichier = "RELEVES/"+nom+".pdf"
        p = canvas.Canvas(fichier,pagesize=letter)
        p.setFont("Helvetica", 14)

        p.translate(inch,inch)
        p.setFont("Helvetica", 30)
        p.setStrokeColorRGB(0.1,0.8,0.1)    
        p.setFillColorRGB(1,0,0) 
        p.drawString(120, 9*inch, "RELEVE DE NOTES") 
        p.setStrokeColorRGB(1,0,0)
        p.setLineWidth(1)
        p.line(0,8.6*inch,6.8*inch,8.6*inch)
 
        """ NOM ET PRENOM """
        p.setFont("Helvetica", 10)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(0.2*inch,7.9*inch, "NOM DE L'ÉTUDIANTS :")


        p.setFont("Helvetica", 15)   
        p.setFillColorRGB(0,0,0) 
        p.drawString(1.9*inch,7.9*inch, nom)

        p.setFont("Helvetica", 10)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(0.2*inch,7.5*inch, "PRENOM DE L'ÉTUDIANTS :")

        p.setFont("Helvetica", 15)   
        p.setFillColorRGB(0,0,0) 
        p.drawString(2.2*inch,7.5*inch, prenom)


        p.setFont("Helvetica", 10)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(0.2*inch,7.1*inch, "SEXE :")

        p.setFont("Helvetica", 15)   
        p.setFillColorRGB(0,0,0) 
        p.drawString(0.9*inch,7.1*inch, str(sexe))


        """ ANNE ACADEMIQUE"""
        p.setFont("Helvetica", 10)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(4.8*inch,7.5*inch, "ANNEE :")

        p.setFont("Helvetica", 10)   
        p.setFillColorRGB(0,0,0) 
        p.drawString(5.5*inch,7.5*inch, "2022-2023")


        """ RECAPITULATIF DES MOYENNES"""
        p.setFont("Helvetica", 11)   
        p.setFillColorRGB(0,0,0) 
        p.drawString(0.1*inch,6.5*inch, "MATIERE")
        p.drawString(1.7*inch,6.5*inch, "DEVOIR")
        p.drawString(2.7*inch,6.5*inch, "EXAMEN")
        p.drawString(3.6*inch,6.5*inch, "PROJET")
        p.drawString(4.6*inch,6.5*inch, "Moyenne")
        p.drawString(5.5*inch,6.5*inch, "Coef")
        p.drawString(6.1*inch,6.5*inch, "Moyenne Coef")

        """ LIGNE VERTICALE """
        p.setStrokeColorCMYK(0,0,0,1)
        p.line(1.5*inch,6.7*inch,1.5*inch,1.2*inch)
        p.line(2.5*inch,6.7*inch,2.5*inch,1.2*inch)
        p.line(3.5*inch,6.7*inch,3.5*inch,1.2*inch)
        p.line(4.4*inch,6.7*inch,4.4*inch,1.2*inch)
        p.line(5.4*inch,6.7*inch,5.4*inch,1.2*inch)
        p.line(6*inch,6.7*inch,6*inch,1.2*inch)

        """ LIGNE HORIZONTALE """
        p.line(0.01*inch,1*inch,7*inch,1*inch)

        """ REMPLISSAGE  """
        row_gap=0.6 
        line_y=5.9
        total=0
        for ligne in donnee_generaux:
            p.setFont("Helvetica", 16)   
            p.setFillColorRGB(0,0,1) 
            p.drawString(0.2*inch,line_y*inch,ligne[2] ) # MATIERE
            p.drawString(1.7*inch,line_y*inch,str(ligne[4]) ) #DEVOIR
            p.drawString(2.7*inch,line_y*inch,str(ligne[5]) ) #EXAMEN
            p.drawString(3.7*inch,line_y*inch,str(ligne[6]) ) #PROJET
            p.drawString(4.5*inch,line_y*inch,str(ligne[7]) ) #MOYENNE
            p.drawString(5.6*inch,line_y*inch,str(ligne[3]) ) # COEFFICIENT
            p.drawString(6.2*inch,line_y*inch,str(ligne[8]) ) #MOYENNE COEFFICIÉ
            line_y=line_y-row_gap


        """ TOTAUX """
        p.setFont("Helvetica", 13)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(0.1*inch,0.6*inch, " Total Coefficient : ")

        p.setFont("Times-Bold", 18) 
        p.setFillColorRGB(1,0,0) 
        p.drawString(1.7*inch,0.6*inch, str(total_coef))
        

        p.setFont("Helvetica", 13)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(2.9*inch,0.6*inch, " Total Moyenne Coefficiée : ")


        p.setFont("Times-Bold", 18)  
        p.setFillColorRGB(1,0,0) 
        p.drawString(5.3*inch,0.6*inch, str(moyenne_total))


        p.setFont("Helvetica", 13)   
        p.setFillColorRGB(0,0,1) 
        p.drawString(0.1*inch,0.09*inch, " MOYENNE GENERALE : ")

        p.setFont("Times-Bold", 18)    
        p.setFillColorRGB(1,0,0) 
        p.drawString(2.3*inch,0.09*inch, str(moyenne_generale))



        p.showPage()
        p.save()

        messagebox.showinfo("","RELEVE GENERER AVEC SUCCESS")
    except:
        messagebox.showinfo("Echec","Echec")
