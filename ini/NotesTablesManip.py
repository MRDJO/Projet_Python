import mysql.connector

def EnregistrementDesNotes(valeurs,info_base):
    try:
        ma_base = mysql.connector.connect(
            host="localhost",
            user = info_base[1],
            password= info_base[2],
            database = info_base[0]
        )
        curseur = ma_base.cursor()

        matricule = valeurs[0]
        id_mat = valeurs[1]
        devoir = valeurs[2]
        examen = valeurs[3]
        projet = valeurs[4]

        Valeurs_test = [matricule,id_mat]
        curseur.execute("SELECT COUNT(*) FROM obtenir WHERE matricule = %s AND id_matiere = %s",Valeurs_test)
        resultat = curseur.fetchone()
        
        if resultat[0] == 0:
            req1 = "INSERT INTO notes(devoir,examen,projet) VALUES (%s,%s,%s)"
            Valeurs = [
                (devoir,examen,projet)
            ]
            curseur.executemany(req1, Valeurs)
            ma_base.commit()


            id_note = curseur.lastrowid
            req2 = "INSERT INTO obtenir(id_note,matricule,id_matiere) VALUES (%s,%s,%s)"
            Valeurs2 =[
                (id_note,matricule,id_mat)
            ]
            curseur.executemany(req2, Valeurs2)
            ma_base.commit()
            return 1
        else:
            return 2
    except:
        ma_base.rollback()
        return 0

def Moyennes(info_base):
    ma_base = mysql.connector.connect(
        host="localhost",
        user = info_base[1],
        password= info_base[2],
        database = info_base[0]
    )
    curseur = ma_base.cursor()

    curseur.execute("SELECT nom,prenom,matieres.code,notes.devoir,notes.examen,notes.projet,(notes.projet + notes.devoir + notes.examen*2)/4 as Moyenne FROM etudiants,obtenir,matieres,notes WHERE obtenir.matricule = etudiants.matricule AND obtenir.id_matiere = matieres.id_matiere AND notes.id_note = obtenir.id_note ORDER BY etudiants.nom ASC")
    Moy = curseur.fetchall()
    return Moy

def SuppressionDeNotes(clees,info_base):
    ma_base = mysql.connector.connect(
        host="localhost",
        user = info_base[1],
        password= info_base[2],
        database = info_base[0]
    )
    curseur = ma_base.cursor()
    matricule = clees[3]
    id_matiere = clees[4]
    id_note = clees[5]
    Valeurs1 = [id_note,matricule,id_matiere]
    Valeurs2 = [id_note]
    try:
        curseur.execute("DELETE FROM obtenir WHERE id_note = %s AND obtenir.matricule = %s AND obtenir.id_matiere = %s",Valeurs1)
        curseur.execute("DELETE FROM notes WHERE id_note = %s",Valeurs2)
        ma_base.commit()
        ligne_sup = curseur.rowcount
        if ligne_sup != 0:
            return 1
        else:
            return 0
    except: 
        ma_base.rollback()
        return 0


def ModificationDeNotes(clees,info_base):
    ma_base = mysql.connector.connect(
        host="localhost",
        user = info_base[1],
        password= info_base[2],
        database = info_base[0]
    )
    curseur = ma_base.cursor()
    devoir = clees[0]
    examen = clees[1]
    projet = clees[2]
    matricule = clees[3]
    id_matiere = clees[4]
    id_note = clees[5]
    Valeurs1 = [devoir,examen,projet,id_matiere,matricule]
    try:
        curseur.execute("UPDATE notes,obtenir SET notes.devoir = %s , notes.examen = %s , notes.projet = %s WHERE obtenir.id_note = notes.id_note AND obtenir.id_matiere = %s AND obtenir.matricule = %s",Valeurs1)
        ma_base.commit()
        return 1
    except:
        ma_base.rollback()
        return 0

