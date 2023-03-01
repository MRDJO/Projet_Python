import os
from tkinter import *
from tkinter import messagebox

import mysql.connector
from ini import recuperation_bdname
from base_de_donnee import *
from base_de_donnee.verification import *

chemin_absolu = os.path.dirname(__file__)
os.chdir(chemin_absolu)

def form_envoye():
    root = var_entry.get() 
    passt = var_entry2.get()
    basee = var_entry3.get()
    return [root,passt,basee]

def entrer():
    liste = form_envoye()
    user = liste[0]
    password = liste[1]
    base_verif = liste[2]
    replay = 1
    essai = 0

    """ VERIFICATION """
    if os.path.isfile("base_info.txt"):
        nom = recuperation_bdname.recuperation_du_nom_de_la_base().strip()
        mdp = recuperation_bdname.recuperation_mdp().strip()
        user = recuperation_bdname.recuperation_user().strip()
        try:
            ma_base = mysql.connector.connect(
                host = "localhost",
                user = user,
                password = mdp,
                database = nom
            )
            messagebox.showinfo("Info","La base de donnee de l'application existe déjà,plus besoin d'en creer;passez à l'application !!")
        except:
            print("Erreur de base de donnee")
    else:
        try:
            if password == "" or password:
                test = verification.verif_exist_base_create_tables(user, password, base_verif)
                if test == 1:
                    base_de_donne_application = base_verif
                    """
                        Stockage du nom de la base de donnee dans un fichier
                    """
                    chemin_absolu = os.path.dirname(__file__)
                    os.chdir(chemin_absolu)
                    fichier_id = open("base_info.txt","a")
                    fichier_id.write("Nom_base:"+base_de_donne_application+"\n")
                    fichier_id.write("user:"+user+"\n")
                    fichier_id.write("mot_de_passe:"+password)
                    fichier_id.close()
                    import menu
                    menu.principale()
        except:
            messagebox.showwarning("ERREUR DE DONNEE","Veuillez entrez un user correct un mot de passe correct !!(:")
            essai +=1 

def ouvrir_app():
    if os.path.isfile("base_info.txt"):
        nom = recuperation_bdname.recuperation_du_nom_de_la_base().strip()
        mdp = recuperation_bdname.recuperation_mdp().strip()
        user = recuperation_bdname.recuperation_user().strip()
        try:
            ma_base = mysql.connector.connect(
                host = "localhost",
                user = user,
                password = mdp,
                database = nom
            )
            app.destroy()
            import menu
            menu.principale()
        except:
            messagebox.showerror("Erreur!!!!","La base de donnee "+nom+" n'existe plus.Consulter la documentation pour trouver une solution")
    else:
        messagebox.showwarning("Avertissement","Veuillez d'abord lancer la creation de la base de donnée OU fermer la fenêtre puis reessayer")    

"""
    Initialisation de tkinter et de la fenêtre principale 

"""
app = Tk()
app.title("Configuration de la base et implementation des tables")
app.geometry("950x550+180+50")

logo = Canvas(app,width=950,height=550,bg="#4683E1")
logo.place(x=0,y=10)
log = Label(logo,text="Configuration",font=("arial",19,"bold"))
log.place(x=20,y=10)

l2 = Label(logo,text="User",font="arial 15 bold",bg="#4683E1",fg="#fff")
l2.place(x=460,y=110)


l3 = Label(app,text="Password",font="arial 15 bold",bg="#4683E1",fg="#fff")
l3.place(x=430,y=200)
 

l4 = Label(app,text="Name database",font="arial 15 bold",bg="#4683E1",fg="#fff")
l4.place(x=400,y=280)


var_entry = StringVar()
var_entry2 = StringVar()
var_entry3 = StringVar()


e1 = Entry(app,textvariable=var_entry,width=50,relief=FLAT,font=('arial',12))
e1.place(x=260,y=150)

e2 = Entry(app,textvariable=var_entry2,show="*",width=50,relief=FLAT,font=("arial",12))
e2.place(x=260,y=230)

e3 = Entry(app,textvariable=var_entry3,width=50,relief=FLAT,font=('arial',12))
e3.place(x=260,y=310)


b = Button(logo,text="Création",font=("arial",10),bg="green",fg="white",relief=FLAT,width="20",command = entrer)
b.place(x=400,y=360)


b2 = Button(logo,text="Application",font=("arial",9),bg="#4683E1",fg="#fff",relief=FLAT,width="10",command = ouvrir_app)
b2.place(x=260,y=420)


app.mainloop()


