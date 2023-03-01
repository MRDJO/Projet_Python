import os
import mysql.connector

def AjoutDeMatiere(data,information):

    ma_base = mysql.connector.connect(
        host = localhost,
        user = information[1],
        password = information[2],
        database = information[0]
    )

    try:
        curseur = ma_base.cursor()

        requete = "INSERT INTO matieres(code,libelle,coefficient) VALUES (%s,%s,%s)"

        curseur.executemany(requete, data)

        ma_base.commit()

        return 1
    except Exception as e:
        return e


def SuppressionDeMatiere(data,information):

    ma_base = mysql.connector.connect(
        host = localhost,
        user = information[1],
        password = information[2],
        database = information[0]
    )

    try:
        curseur = ma_base.cursor()

        requete = "DELETE FROM matieres WHERE "

        curseur.executemany(requete, data)

        ma_base.commit()

        return 1
    except Exception as e:
        return e
