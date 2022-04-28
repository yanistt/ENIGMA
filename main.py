
from tkinter import*
from tkinter import ttk #LE GUI UTILISÉ POUR L'INTERFACE GRAPHIQUE
import tkinter.messagebox as msgb #POP UP BOXES UTILISÉ POUR LES MESSAGES D'ERREUR
import numpy as np #BIBLIHOTHÉQUE PYTHON POUR CRÉER DES VECTEURS 1D ET 2D
import re

#***************************************************************************************************************************
#ON DÉCLARE LES STRUCTURES NÉCESSAIRES AU PROJET
Rotor_3 = np.array(
    [[1, 16, 5, 17, 20, 8, -2, 2, 14, 6, 2, -5, -12, -10, 9, 10, 5, -9, 1, -14, -2, -10, -6, 13, -10, -23],
     [12, -1, 23, 10, 2, 14, 5, -5, 9, -2, -13, +10, -2, -8, 10, -6, 6, -16, 2, -1, -17, -5, -14, -9, -20,
      -10]])
Rotor_2 = np.array(
    [[3, 17, 22, 18, 16, 7, 5, 1, -7, 16, -3, 8, 2, 9, 2, -5, -1, -13, -12, -17, -11, -4, 1, -10, -19, -25],
     [25, 7, 17, -3, 13, 19, 12, 3, -1, 11, 5, -5, -7, 10, -2, 1, -2, 4, -17, -8, -16, -18, -9, -1, -22, -16]])
Rotor_1 = np.array(
    [[10, 21, 5, -17, 21, -4, 12, 16, 6, -3, 7, -7, 4, 2, 5, -7, -11, -17, -9, -6, -9, -19, 2, -3, -21, -4],
     [17, 4, 19, 21, 7, 11, 3, -5, 7, 9, -10, 9, 17, 6, -6, -2, -4, -7, -12, -5, 3, 4, -21, -16, -2, -21]])
Reflector = np.array(
    [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25])
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W', 'X', 'Y', 'Z']
global MsgDecry
global MsgCry
index = 0
global setting
setting = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
global control
control = 0
global position
position = 0
global message
message = ''
global config
config = [0, 0]
global ready
ready = 0
#***************************************************************************************************************************

def initialiser() :
    #CETTE FONCTION SERT À INITIALISER LES DONNÉES DÉS L'OUVERTURE DE L'ÉXECUTABLE
    global Rotor_1
    global Rotor_2
    global Rotor_3
    global setting
    global config

    Rotor_3 = np.array(
        [[1, 16, 5, 17, 20, 8, -2, 2, 14, 6, 2, -5, -12, -10, 9, 10, 5, -9, 1, -14, -2, -10, -6, 13, -10, -23],
         [12, -1, 23, 10, 2, 14, 5, -5, 9, -2, -13, +10, -2, -8, 10, -6, 6, -16, 2, -1, -17, -5, -14, -9, -20,
          -10]])
    Rotor_2 = np.array(
        [[3, 17, 22, 18, 16, 7, 5, 1, -7, 16, -3, 8, 2, 9, 2, -5, -1, -13, -12, -17, -11, -4, 1, -10, -19, -25],
         [25, 7, 17, -3, 13, 19, 12, 3, -1, 11, 5, -5, -7, 10, -2, 1, -2, 4, -17, -8, -16, -18, -9, -1, -22, -16]])
    Rotor_1 = np.array(
        [[10, 21, 5, -17, 21, -4, 12, 16, 6, -3, 7, -7, 4, 2, 5, -7, -11, -17, -9, -6, -9, -19, 2, -3, -21, -4],
         [17, 4, 19, 21, 7, 11, 3, -5, 7, 9, -10, 9, 17, 6, -6, -2, -4, -7, -12, -5, 3, 4, -21, -16, -2, -21]])

    config = [0, 0]
    setting = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#***************************************************************************************************************************

def verf(t):
    y = 0
    #ON VÉRFIE SI LE DÉCALGE ENTRÉE EST UN ENTIER NÉGATIF OU POSITIF, SINON UNE EXCEPTION EST ENVOYÉ
    try:
        int(t[0][2])
        it_is1 = True
    except ValueError:
        it_is1 = False
    try:
        int(t[1][2])
        it_is2 = True
    except ValueError:
        it_is2 = False
    try:
        int(t[2][2])
        it_is3 = True
    except ValueError:
        it_is3 = False
    #VÉRIFICATION DE L'ORTHOGRAPHE SAISIE PAR L'UTILISATEUR (TOUS LES CAS SONT PRIS EN CONSIDÉRATION)
    if (t[0][0] != 'R1') & (t[0][0] != 'R2') & (t[0][0] != 'R3') & (t[0][0] != 'r1') & (t[0][0] != 'r2') & (
            t[0][0] != 'r3') \
            | (t[1][0] != 'R1') & (t[1][0] != 'R2') & (t[1][0] != 'R3') & (t[1][0] != 'r1') & (t[1][0] != 'r2') & (
            t[1][0] != 'r3') \
            | (t[2][0] != 'R1') & (t[2][0] != 'R2') & (t[2][0] != 'R3') & (t[2][0] != 'r1') & (t[2][0] != 'r2') & (
            t[2][0] != 'r3'):
        y = y + 1
    if (t[0][1] != 'G') & (t[0][1] != 'D') & (t[0][1] != 'g') & (t[0][1] != 'd') \
            | (t[1][1] != 'D') & (t[1][1] != 'G') & (t[1][1] != 'g') & (t[1][1] != 'd') \
            | (t[2][1] != 'D') & (t[2][1] != 'G') & (t[2][1] != 'g') & (t[2][1] != 'd'):
        y = y + 1
    if (it_is1 == False) | (it_is2 == False) | (it_is3 == False):
        y = y + 1
    if (t[0][0].upper() == t[2][0].upper()) | (t[0][0].upper() == t[1][0].upper()) | (t[1][0].upper() == t[2][0].upper()):
        y = y + 1
    if y == 0:
        #DANS LE CAS OÚ LA VARIABLE RESTE INITIALISÉE À 0, CELA VEUT DIRE QU'AUCUNE FAUTE DE SAISIE N'A ÉTÉ FAITE
        setting = t.copy()
        # ON COPIE LA CONFIGURATION DE LA CLÉ DANS UNE VARIABLE GLOBALE SETTING POUR L'UTILISER DANS D'AYTRES FONCTIONS
    else:
        #SI UNE ERREUR DE SAISIE OCCURE, UN MESSAGE POP-UP EST ENVOYÉ
        msgb.showwarning('Erreur!', 'Erreur dans votre cle! \n Veuillez re-rentrer la cle')
    return y

#***************************************************************************************************************************

def configurer():
    global Rotor_1
    global Rotor_2
    global Rotor_3
    global setting
    global ready

    initialiser()
    #ÉQUIVQLENT À DES OUTPUT, ON RÉCUPÉRE LA SAISIE DE L'UTILISATEUR DANS DES VARIABLES
    Rtr1 = ligne_saisie1.get()
    ort1 = ligne_saisie2.get()
    dcl1 = ligne_saisie3.get()

    Rtr2 = ligne_saisie4.get()
    ort2 = ligne_saisie5.get()
    dcl2 = ligne_saisie6.get()

    Rtr3 = ligne_saisie7.get()
    ort3 = ligne_saisie8.get()
    dcl3 = ligne_saisie9.get()

    T = np.array([[Rtr1, ort1, dcl1], [Rtr2, ort2, dcl2], [Rtr3, ort3, dcl3]])
    #ON PLACE LES VARIABLES DANS UN TABLEAU
    setting = T.copy()
    y = 0
    y = verf(T) #ON VÉRIFIE LA VALIDITÉ DE LA CLÉ
    if y == 0:
        ready = 1
        j = 0
        while j < 3:
            rotor = setting[j][0]
            decalage = int(setting[j][2])
            direction = setting[j][1]

            if (rotor == 'r1') | (rotor == 'R1'):
                if (direction == 'D') | (direction == 'd'):
                    Rotor_1 = np.roll(Rotor_1, decalage, axis=1)
                else:
                    decalage = decalage * (-1)
                    Rotor_1 = np.roll(Rotor_1, decalage, axis=1)
            if (rotor == 'r2') | (rotor == 'R2'):
                if (direction == 'D') | (direction == 'd'):
                    Rotor_2 = np.roll(Rotor_2, decalage, axis=1)
                else:
                    decalage = decalage * (-1)
                    Rotor_2 = np.roll(Rotor_2, decalage, axis=1)
            if (rotor == 'r3') | (rotor == 'R3'):
                if (direction == 'D') | (direction == 'd'):
                    Rotor_3 = np.roll(Rotor_3, decalage, axis=1)
                else:
                    decalage = decalage * (-1)
                    Rotor_3 = np.roll(Rotor_3, decalage, axis=1)
            j = j + 1
        #ON AFFFICHE LA CONFIGURATION GRAPHIQUEMENT
        for i in range(0, Colonne):
            for j in range(0, Ligne):
                Saisie1[i][j] = ttk.Entry(frame_r3, width=6) # CHAQUE CASE DES TABLEAUX EST DÉFINIE COMME UN WIDGET
                if j == 0: k = Rotor_3[j + 1][i]
                if j == 1: k = Rotor_3[j - 1][i]
                w = Saisie3[i][j].get()
                if (len(w) > 1) : Saisie3[i][j].delete(0,2)
                if (len(w) > 2) : Saisie3[i][j].delete(0, 3)
                else : Saisie3[i][j].delete(0,1)
                Saisie1[i][j].insert(0,k)    # ON Y INSÉRE LES VALEURS INITIALISÉES PRÉCEDEMMENT
                Saisie1[i][j].grid(column=i, row=j, pady=3, padx=1,) # ON CONFIGURE CHAQUE CASE/STRUCTURE
        for i in range(0, Colonne):
            for j in range(0, Ligne):
                Saisie1[i][j] = ttk.Entry(frame_r2, width=6)
                if j == 0: k = Rotor_2[j + 1][i]
                if j == 1: k = Rotor_2[j - 1][i]
                w = Saisie2[i][j].get()
                if (len(w) > 1): Saisie2[i][j].delete(0, 2)
                if (len(w) > 2):Saisie2[i][j].delete(0, 3)
                else : Saisie2[i][j].delete(0, 1)
                Saisie1[i][j].insert(0,k)
                Saisie1[i][j].grid(column=i, row=j, pady=3, padx=1, sticky=E)
        for i in range(0, Colonne):
            for j in range(0, Ligne):
                Saisie1[i][j] = ttk.Entry(frame_r1, width=6)
                if j == 0: k = Rotor_1[j + 1][i]
                if j == 1: k = Rotor_1[j - 1][i]
                w = Saisie1[i][j].get()
                if (len(w) > 1): Saisie1[i][j].delete(0, 2)
                if (len(w) > 2):Saisie1[i][j].delete(0, 3)
                else : Saisie1[i][j].delete(0, 1)
                Saisie1[i][j].insert(0,k)
                Saisie1[i][j].grid(column=i, row=j, pady=3, padx=1)
        for i in range(0, Colonne):
            for j in range(0, 1):
                Saisie4[i][j] = ttk.Entry(frame_ref, width=6)
                k = Reflector[i]
                Saisie4[i][j].insert(0, k)
                Saisie4[i][j].grid(column=i, row=j, pady=3, padx=1)
        for i in range(0, Colonne):
            for j in range(0, 1):
                Saisie5[i][j] = ttk.Entry(frame_alp, width=6)
                k = alphabet[i]
                Saisie5[i][j].insert(0, k)
                Saisie5[i][j].grid(column=i, row=j, pady=3, padx=1)


#***************************************************************************************************************************

def parcour(ind):
    a=Rotor_1[0][ind]
    Saisie[ind][1] = ttk.Entry(frame_r1, style="EntryStyle2.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
    Saisie[ind][1].grid(column=ind, row=1, pady=3, padx=1) #REPOSITIONNEMENT
    Saisie[ind][1].insert(0, a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
    ind = Rotor_1[0][ind] + ind + 26
    ind = ind % 26
    a=Rotor_2[0][ind]
    Saisie[ind][1] = ttk.Entry(frame_r2, style="EntryStyle2.TEntry", width=6)
    Saisie[ind][1].grid(column=ind, row=1, pady=3, padx=1)
    Saisie[ind][1].insert(0, a)
    ind = Rotor_2[0][ind] + ind + 26
    ind = ind % 26
    a=Rotor_3[0][ind]
    Saisie[ind][1] = ttk.Entry(frame_r3, style="EntryStyle2.TEntry", width=6)
    Saisie[ind][1].grid(column=ind, row=1, pady=3, padx=1)
    Saisie[ind][1].insert(0, a)
    ind = Rotor_3[0][ind] + ind + 26
    ind = ind % 26
    a=Reflector[ind]
    Saisie[ind][0] = ttk.Entry(frame_ref, style="EntryStyle2.TEntry", width=6)
    Saisie[ind][0].grid(column=ind, row=0, pady=3, padx=1)
    Saisie[ind][0].insert(0, a)
    ind = Reflector[ind] + ind + 26
    ind = ind % 26
    a=Rotor_3[1][ind]
    Saisie[ind][0] = ttk.Entry(frame_r3, style="EntryStyle1.TEntry", width=6)
    Saisie[ind][0].grid(column=ind, row=0, pady=3, padx=1)
    Saisie[ind][0].insert(0, a)
    ind = Rotor_3[1][ind] + ind + 26
    ind = ind % 26
    a=Rotor_2[1][ind]
    Saisie[ind][0] = ttk.Entry(frame_r2, style="EntryStyle1.TEntry", width=6)
    Saisie[ind][0].grid(column=ind, row=0, pady=3, padx=1)
    Saisie[ind][0].insert(0, a)
    ind = Rotor_2[1][ind] + ind + 26
    ind = ind % 26
    a=Rotor_1[1][ind]
    Saisie[ind][0] = ttk.Entry(frame_r1, style="EntryStyle1.TEntry", width=6)
    Saisie[ind][0].grid(column=ind, row=0, pady=3, padx=1)
    Saisie[ind][0].insert(0, a)
    ind = Rotor_1[1][ind] + ind + 26
    ind = ind % 26


    return ind
#***************************************************************************************************************************

def changer_configuration():
    global Rotor_1
    global Rotor_2
    global Rotor_3
    global setting
    global config

    if config[1] < 25:
        config[1] = config[1] + 1
    else:
        config[1] = 0
        if config[0] < 2 :
            config[0] = config[0] +1
        else :
            config[0] = 0

    rotor = setting[config[0]][0]
    direction = setting[config[0]][1]

    if (rotor == 'r1') | (rotor == 'R1'):
        if (direction == 'D') | (direction == 'd'):
            Rotor_1 = np.roll(Rotor_1, 1, axis=1)
        else:
            Rotor_1 = np.roll(Rotor_1, -1, axis=1)


    if (rotor == 'r2') | (rotor == 'R2'):
        if (direction == 'D') | (direction == 'd'):
            Rotor_2 = np.roll(Rotor_2, 1, axis=1)
        else:
            Rotor_2 = np.roll(Rotor_2, -1, axis=1)

    if (rotor == 'r3') | (rotor == 'R3'):
        if (direction == 'D') | (direction == 'd'):
            Rotor_3 = np.roll(Rotor_3, 1, axis=1)
        else:
            Rotor_3 = np.roll(Rotor_3, -1, axis=1)


#***************************************************************************************************************************

def encrypter():

    global control
    global MsgDecry
    global MsgCry
    global position
    global message
    global config
    global setting
    global ready

    if (ready==1) :
        position = 0
        control = 1
        ligne_saisie11.delete(0, END)
        MsgDecry = ligne_saisie10.get()
        MsgDecry = MsgDecry.upper()
        message = list(str(MsgDecry))
        if re.match("^[a-zA-Z ]*$", MsgDecry) : k=0
        else: k=1

        if(MsgDecry == '') | k==1 :
            if (MsgDecry == '') :
                msgb.showwarning('Erreur!', ' Veuillez introduire votre messge a décrypter')
            else :
                msgb.showwarning('Erreur!', ' Le champs de saise n\'accepte que les lettres et les espaces!')
        else :
            lettre = message[0]
            if (lettre != ' '):
                ind = alphabet.index(lettre)
                a=alphabet[ind]
                Saisie5[ind][0]= ttk.Entry(frame_alp, style="EntryStyle2.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
                Saisie5[ind][0].grid(column=ind,row=0,pady= 3, padx= 1) #ON REPOSITIONNE LA CASE
                Saisie5[ind][0].insert(0,a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
                lettre_res =alphabet[parcour(ind)]
                ind = alphabet.index(lettre_res)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle1.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1) #ON REPOSITIONNE LA CASE
                Saisie5[ind][0].insert(0, a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
                MsgCry = [lettre_res]
                changer_configuration()
            else:
                MsgCry= [' ']
        MsgCry = "".join(MsgCry)
        ligne_saisie11.insert(0, MsgCry)
    else :
        msgb.showwarning('Erreur!', ' Veuillez configurer la machine avant !')


#***************************************************************************************************************************

def decrypter():

    global control
    global MsgDecry
    global MsgCry
    global position
    global message
    global config
    global setting
    global ready

    if (ready == 1):
        position = 0
        control = 2
        ligne_saisie10.delete(0, END)
        MsgCry = ligne_saisie11.get()
        MsgCry = MsgCry.upper()
        message = list(str(MsgCry))
        if re.match("^[a-zA-Z ]*$", MsgCry) : k=0
        else: k=1

        if(MsgCry == '') | k==1:
            if (MsgCry == '') :
                msgb.showwarning('Erreur!', ' Veuillez introduire votre messge a décrypter')
            else :
                msgb.showwarning('Erreur!', ' Le champs de saise n\'accepte que les lettres et les espaces!')
        else :
            lettre = message[0]
            if (lettre != ' '):
                ind = alphabet.index(lettre)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle2.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1) #ON REPOSITIONNE LA CASE
                Saisie5[ind][0].insert(0, a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
                lettre_res =alphabet[parcour(ind)]
                ind = alphabet.index(lettre_res)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle1.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1) #ON REPOSITIONNE LA CASE
                Saisie5[ind][0].insert(0, a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
                MsgDecry = [lettre_res]
                changer_configuration()


            else:
                MsgDecry= [' ']
        MsgDecry = "".join(MsgDecry)
        ligne_saisie10.insert(0, MsgDecry)
    else :
        msgb.showwarning('Erreur!', ' Veuillez configurer la machine avant !')


#***************************************************************************************************************************

def etsuivante_dec():
    global position
    global MsgDecry
    global message
    global ready


    position = position + 1
    MsgDecry = list(str(MsgDecry))
    if position < len(message):
            lettre = message[position]
            if (lettre != ' '):
                ind = alphabet.index(lettre)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle2.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1) #ON REPOSITIONNE LA CASE
                Saisie5[ind][0].insert(0, a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
                lettre_res = alphabet[parcour(ind)]
                ind = alphabet.index(lettre_res)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle1.TEntry", width=6) #ON APPLIQUE UNE COULEUR À LA CASE
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1) #ON REPOSITIONNE LA CASE
                Saisie5[ind][0].insert(0, a) #ON Y RE-INSÉRE LA VALEUR INITIALE, CAR ELLE A ÉTÉ ECRASÉ EN METTANT LA COULEUR
                MsgDecry = MsgDecry + [lettre_res]
                changer_configuration()
            else:
                MsgDecry = MsgDecry + [' ']
            ligne_saisie10.delete(0, END)
            MsgDecry = "".join(MsgDecry)
            ligne_saisie10.insert(0, MsgDecry)

#***************************************************************************************************************************

def etsuivante_enc():
    global position
    global MsgCry
    global message
    global ready

    position = position + 1
    MsgCry = list(str(MsgCry))
    if position < len(message):
            lettre = message[position]
            if (lettre != ' '):
                ind = alphabet.index(lettre)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle2.TEntry", width=6)
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1)
                Saisie5[ind][0].insert(0, a)
                lettre_res = alphabet[parcour(ind)]
                ind = alphabet.index(lettre_res)
                a = alphabet[ind]
                Saisie5[ind][0] = ttk.Entry(frame_alp, style="EntryStyle1.TEntry", width=6)
                Saisie5[ind][0].grid(column=ind, row=0, pady=3, padx=1)
                Saisie5[ind][0].insert(0, a)
                MsgCry = MsgCry + [lettre_res]
                changer_configuration()
            else:
                MsgCry = MsgCry + [' ']
            ligne_saisie11.delete(0, END)
            MsgCry = "".join(MsgCry)
            ligne_saisie11.insert(0, MsgCry)
#***************************************************************************************************************************

def etsuivante():
    global Rotor_1
    global Rotor_2
    global Rotor_3
    global setting
    global config
    #ON RÉAFFICHE LES 5 STRUCTURES POUR FAIRE APPARAITRE LES CHANGEMENTS
    for i in range(0, Colonne):
        for j in range(0, 1):
            Saisie4[i][j] = ttk.Entry(frame_ref, width=6)
            k = Reflector[i]
            Saisie4[i][j].insert(0, k)
            Saisie4[i][j].grid(column=i, row=j, pady=3, padx=1)
    for i in range(0, Colonne):
        for j in range(0, 1):
            Saisie5[i][j] = ttk.Entry(frame_alp, width=6)
            k = alphabet[i]
            Saisie5[i][j].insert(0, k)
            Saisie5[i][j].grid(column=i, row=j, pady=3, padx=1)
    for i in range(0, Colonne):
        for j in range(0, Ligne):
            Saisie3[i][j] = ttk.Entry(frame_r3, width=6)
            if j == 0: k = Rotor_3[j + 1][i]
            if j == 1: k = Rotor_3[j - 1][i]
            Saisie3[i][j].insert(0, k)
            Saisie3[i][j].grid(column=i, row=j, pady=3, padx=1)
    for i in range(0, Colonne):
        for j in range(0, Ligne):
            Saisie2[i][j] = ttk.Entry(frame_r2, width=6, )
            if j == 0: k = Rotor_2[j + 1][i]
            if j == 1: k = Rotor_2[j - 1][i]
            Saisie2[i][j].insert(0, k)
            Saisie2[i][j].grid(column=i, row=j, pady=3, padx=1, sticky=E)
    for i in range(0, Colonne):
        for j in range(0, Ligne):
            Saisie1[i][j] = ttk.Entry(frame_r1, width=6)

            if j == 0: k = Rotor_1[j + 1][i]
            if j == 1: k = Rotor_1[j - 1][i]
            Saisie1[i][j].insert(0, k)
            Saisie1[i][j].grid(column=i, row=j, pady=3, padx=1)

    if (control==1) :
        etsuivante_enc()
    else :
        if (control==2) :
            etsuivante_dec()
        else :
            msgb.showwarning('Erreur!', ' Veuillez sélectionner l opération\n à effectuer "encrypter" ou "decrypter"')

#***************************************************************************************************************************
#================================
#Personnalisation de la fenêtres
#================================
from tkinter import Label, PhotoImage
window = Tk()
window.title("ENIGMA")
window.geometry("1200x700")
window.minsize(1200, 700)
window.iconbitmap("6391254.ico")
window.config(background='#FAF6DC')
#================================
#Création de la frame
#================================
# ON DIVISE LA FENÊTRE PRINCIPALE EN PLUSIEURS CADRES, ET Chaque COUCHE CONTIENDRA UNE STRUCTURE (TABLEAU, IMAGE, TEXTE, ...)
frame = Frame(window, bg="#FAF6DC")#, bd=1, relief=SUNKEN )
frame.pack(side=TOP)
frame_reftxt=Frame(window,bg="#FAF6DC")
frame_reftxt.pack()
frame_ref=Frame(window,bg="#FAF6DC")
frame_ref.pack()
frame_r3txt=Frame(window,bg="#FAF6DC")
frame_r3txt.pack()
frame_r3=Frame(window,bg="#FAF6DC")
frame_r3.pack()
frame_r2txt=Frame(window,bg="#FAF6DC")
frame_r2txt.pack()
frame_r2=Frame(window,bg="#FAF6DC")
frame_r2.pack()
frame_r1txt=Frame(window,bg="#FAF6DC")
frame_r1txt.pack()
frame_r1=Frame(window,bg="#FAF6DC")
frame_r1.pack()
frame_alptxt=Frame(window,bg="#FAF6DC")
frame_alptxt.pack()
frame_alp=Frame(window,bg="#FAF6DC")
frame_alp.pack()

frame_cle=Frame(window,bg="#FAF6DC")
frame_cle.pack()

frame_text=Frame(window,bg="#FAF6DC")
frame_text.pack()

framecrytxt = Frame(window, bg="#FAF6DC")#, bd=1, relief=SUNKEN )
framecrytxt.pack()

framecry = Frame(window, bg="#FAF6DC")#, bd=1, relief=SUNKEN )
framecry.pack()

frame1 = Frame(window, bg="#FAF6DC")#, bd=1, relief=SUNKEN )
frame1.pack()

framedecrytxt = Frame(window, bg="#FAF6DC")#, bd=1, relief=SUNKEN )
framedecrytxt.pack()

framedecry = Frame(window, bg="#FAF6DC")#, bd=1, relief=SUNKEN )
framedecry.pack()
#ON INSERE UNE IMAGE DANS L'INTERFACE
image = PhotoImage(file="fléche.png").subsample(3)
canvas1 = Canvas(frame_alptxt, width=100, height=40,bg="#FAF6DC",bd=0,highlightthickness=0)
canvas1.create_image(50, 20, image=image)
canvas1.pack(expand=YES)
#================================
#Texte sur la fenêtre
#================================
# ON INSÉRE LES CHAINES DE CARACTÉRES DANS LEURS CADRES CORRESPONDANTS
textt= Label(frame_cle, text=' ~~ LA CLÉ ~~', font=("GNUTypewriter",15),bg="#FAF6DC" )
textt.pack(pady=6)
texte1 = Label(frame_text, text = ' ( ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
R1 = StringVar()
ligne_saisie1 = Entry(frame_text, textvariable = R1 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie1.pack(side = LEFT, padx = 1, pady = 1)

texte1 = Label(frame_text, text = ' , ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
O1 = StringVar()
ligne_saisie2 = Entry(frame_text, textvariable = O1 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie2.pack(side = LEFT, padx = 1, pady = 1)
ort1 = ligne_saisie2.get()
texte1 = Label(frame_text, text = ' , ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
D1 = StringVar()
ligne_saisie3 = Entry(frame_text, textvariable = D1 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie3.pack(side = LEFT, padx = 1, pady = 1)
dcl1 = ligne_saisie3.get()

texte1 = Label(frame_text, text = ' ) ( ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
R2 = StringVar()
ligne_saisie4 = Entry(frame_text, textvariable = R2 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie4.pack(side = LEFT, padx = 1, pady = 1)
Rtr2 = ligne_saisie4.get()
texte1 = Label(frame_text, text = ' , ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
O2 = StringVar()
ligne_saisie5 = Entry(frame_text, textvariable = O2 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie5.pack(side = LEFT, padx = 1, pady = 1)
ort2 = ligne_saisie5.get()
texte1 = Label(frame_text, text = ' , ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
D2 = StringVar()
ligne_saisie6 = Entry(frame_text, textvariable = D2 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie6.pack(side = LEFT, padx = 1, pady = 1)
dcl2 = ligne_saisie6.get()
texte1 = Label(frame_text, text = ' ) ( ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)

R3= StringVar()
ligne_saisie7 = Entry(frame_text, textvariable = R3 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie7.pack(side = LEFT, padx = 1, pady = 1)
Rtr3=ligne_saisie7.get()
texte1 = Label(frame_text, text = ' , ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
O3 = StringVar()
ligne_saisie8 = Entry(frame_text, textvariable = O3 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie8.pack(side = LEFT, padx = 1, pady = 1)
ort3 = ligne_saisie8.get()
texte1 = Label(frame_text, text = ' , ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)
D3 = StringVar()
ligne_saisie9 = Entry(frame_text, textvariable = D3 , bg = 'white', fg= 'black', font="GNUTypewriter",width=2)
ligne_saisie9.pack(side = LEFT, padx = 1, pady = 1)
dcl3=ligne_saisie9.get()
texte1 = Label(frame_text, text = ' ) ' , font = ("Alibi",20) ,bg="#FAF6DC")
texte1.pack(side = LEFT, padx = 1, pady = 1)

MessageClair  = StringVar()
ligne_saisie10 = Entry(framecry, textvariable = MessageClair , bg = 'white', fg= 'black', font="GNUTypewriter",width=20,relief=RIDGE)
ligne_saisie10.pack(side = LEFT, padx = 1, pady = 1)

MessageCry  = StringVar()
ligne_saisie11 = Entry(framedecry, textvariable = MessageCry , bg = 'white', fg= 'black', font="GNUTypewriter",width=20,relief=RIDGE)
ligne_saisie11.pack(side = LEFT, padx = 1, pady = 1)

texte_lab = Label(frame, text = "Bienvenue sur ENIGMA", font = ("Type Keys Filled", 30), bg = "#FAF6DC", fg = "#713C3C")
texte_lab.pack(side=LEFT)
texte_lab4 = Label(frame_reftxt, text = "réflécteur", font = ("GNUTypewriter",10), bg = "#FAF6DC", fg = "black")
texte_lab4.pack(side=LEFT)
texte_lab4 = Label(frame_r3txt, text = "rotor3", font = ("GNUTypewriter",10), bg = "#FAF6DC", fg = "black")
texte_lab4.pack(side=LEFT)
texte_lab4 = Label(frame_r2txt, text = "rotor2", font = ("GNUTypewriter",10), bg = "#FAF6DC", fg = "black")
texte_lab4.pack(side=LEFT)
texte_lab4 = Label(frame_r1txt, text = "rotor1", font = ("GNUTypewriter",10), bg = "#FAF6DC", fg = "black")
texte_lab4.pack(side=LEFT)

texte_lab4 = Label(framecrytxt, text = "Message en clair", font = ("GNUTypewriter",16), bg = "#FAF6DC", fg = "black")
texte_lab4.pack(side=LEFT)
texte_lab4 = Label(framedecrytxt, text = "Message crypté", font = ("GNUTypewriter",16), bg = "#FAF6DC", fg = "black")
texte_lab4.pack(side=LEFT)


#================================
#Ajouter un bouton
#================================
crypter_btn = Button(frame1, text="Encrypter", font=("GNUTypewriter", 15), bg="#824F4F", fg="#FAF6DC", command = encrypter)
crypter_btn.pack(side=LEFT, padx=10, pady=8)
crypter_btn1 = Button(frame1, text="Configurer les rotors", font=("GNUTypewriter", 15), bg="#9C7777", fg="#FAF6DC", command = configurer)
crypter_btn1.pack(side=LEFT, padx=10)
crypter_btn2 = Button(frame1, text="Etape suivante", font=("GNUTypewriter", 15), bg="#824F4F", fg="#FAF6DC", command = etsuivante)
crypter_btn2.pack(side=LEFT, padx=10)
crypter_btn3 = Button(frame1, text="Décrypter", font=("GNUTypewriter", 15), bg="#9C7777", fg="#FAF6DC", command = decrypter)
crypter_btn3.pack(side=LEFT, padx=10)

#============================================================================================##


#===========================================================================================#
Colonne = 26
Ligne = 2
Saisie = np.full((27,2),"",dtype=object)
Saisie4 = np.full((27,2),"",dtype=object)
Saisie5 = np.full((27,2),"",dtype=object)
Saisie3 = np.full((27,3),"         ",dtype=object)
Saisie2 = np.full((27,3),"         ",dtype=object)
Saisie1 = np.full((27,3),"         ",dtype=object)
estyle_aller = ttk.Style()
#DEFINITION DU STYLE DE COULEUR ROUGE
estyle_aller.element_create("plain.field", "from", "clam")
estyle_aller.layout("EntryStyle1.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'1', 'sticky': 'nswe'})])
estyle_aller.configure("EntryStyle1.TEntry",
                 background="black",
                 foreground="black",
                 fieldbackground="#73C2FB")


#DÉFINITION DU STYLE DE COULEUR VERT
estyle_retour = ttk.Style()
estyle_retour.layout("EntryStyle2.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'1', 'sticky': 'nswe'})])
estyle_retour.configure("EntryStyle2.TEntry",
                 background="grey",
                 foreground="black",
                 fieldbackground="#BE302B")


#FONCTION D'AFFICHAGE DES ROTORS, RÉFLÉCTEURS, ALPHABET
for i in range (0,Colonne):
    for j in range (0, 1):
        Saisie4[i][j]=ttk.Entry(frame_ref,width=6)
        k=Reflector[i]
        Saisie4[i][j].insert(0,k)
        Saisie4[i][j].grid(column=i,row=j,pady= 3, padx= 1)
for i in range (0,Colonne):
    for j in range (0, 1):
        Saisie5[i][j]=ttk.Entry(frame_alp,width=6)
        k=alphabet[i]
        Saisie5[i][j].insert(0,k)
        Saisie5[i][j].grid(column=i,row=j,pady= 3, padx= 1)
for i in range (0,Colonne):
    for j in range (0, Ligne):
        Saisie3[i][j]=ttk.Entry(frame_r3,width=6)
        if j==0 : k=Rotor_3[j+1][i]
        if j==1 : k=Rotor_3[j-1][i]
        Saisie3[i][j].insert(0,k)
        Saisie3[i][j].grid(column=i,row=j,pady= 3, padx= 1)
for i in range (0,Colonne):
    for j in range (0, Ligne):
        Saisie2[i][j]=ttk.Entry(frame_r2,width=6,)
        if j==0 : k=Rotor_2[j+1][i]
        if j==1 : k=Rotor_2[j-1][i]
        Saisie2[i][j].insert(0,k)
        Saisie2[i][j].grid(column=i,row=j,pady= 3, padx= 1, sticky = E)
for i in range (0,Colonne):
    for j in range (0, Ligne):
        Saisie1[i][j]=ttk.Entry(frame_r1,width=6)

        if j==0 : k=Rotor_1[j+1][i]
        if j==1 : k=Rotor_1[j-1][i]
        Saisie1[i][j].insert(0,k)
        Saisie1[i][j].grid(column=i,row=j,pady= 3, padx= 1)




#EXÉCUTION DE LA FENÊTRE
window.mainloop()