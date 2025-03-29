# Modules ---------------------------------------------------------------
from random import randint
from tkinter import Tk, Menu, Canvas, Label, Entry, StringVar, Button, Text, SUNKEN, PhotoImage
from PIL import Image, ImageTk
from winsound import PlaySound, SND_ASYNC
import time


# Fonctions ---------------------------------------------------------------


def creer_fenetre():
    global fenetre
    fenetre = Tk()
    fenetre.title("Random bullet")
    fenetre.resizable(False, False)
    return fenetre


def nettoyer_fenetre():
    for widget in fenetre.winfo_children():
        widget.destroy()


def accueil():
    global zone_graphique, titre, bouton_1, bouton_2, bouton_3, vie1, vie2, psdtour, inv1, inv2, pseudo1, pseudo2, utilisation, utilisationvoir, jeu, utilisationbloquer, rejouer1, rejouer2, degatsx2, balleapres, fb, vb, nbtour, victoire, item, bottour

    nettoyer_fenetre()
    vie1 = 4
    vie2 = 4
    nbtour = 1
    vie1 = 4
    vie2 = 4
    vb = 1
    fb = 2
    degatsx2 = False
    balleapres = False
    rejouer1 = False
    rejouer2 = False
    victoire = False
    item = ["2damages", "bloquer", "vie", "voir", "skip"]
    inv1 = []
    inv2 = []
    utilisation = 0
    utilisationvoir = 0
    utilisationbloquer = 0
    bottour = False

    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=5, column=0, columnspan=3)

    titre = Label(fenetre, text="Random bullet", fg="white", bg='#272727', font=("Arial", 32, "bold"))
    titre.grid(row=0, column=1)

    bouton_1 = PhotoImage(file="images/bouton1.png")
    id_image = zone_graphique.create_image(600, 200, anchor="c", image=bouton_1)
    zone_graphique.tag_bind(id_image, "<Button-1>", lambda event: ecran_bot())

    bouton_2 = PhotoImage(file="images/bouton2.png")
    id_image2 = zone_graphique.create_image(600, 350, anchor="c", image=bouton_2)
    zone_graphique.tag_bind(id_image2, "<Button-1>", lambda event: ecran_ami())

    bouton_3 = PhotoImage(file="images/bouton3.png")
    id_image3 = zone_graphique.create_image(600, 500, anchor="c", image=bouton_3)
    zone_graphique.tag_bind(id_image3, "<Button-1>", lambda event: comment_jouer())

    return zone_graphique, titre, bouton_1, bouton_2, bouton_3


def ecran_bot():
    global zone_graphique, fond_image, valider, retour, pseudo1, pseudo2, joueur, psdtour
    nettoyer_fenetre()
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=5, column=0, columnspan=3)

    fond_image = PhotoImage(file="images/fond.png")
    zone_graphique.create_image(600, 300, anchor="c", image=fond_image)

    titre = Label(fenetre, text="Pseudo du joueur", fg="white", bg='#5A5A5A', font="Arial 24 bold")
    titre.place(relx=0.5, y=175, anchor="center")

    entrerpseudo = Entry(fenetre, font=("Arial", 16), width=20, bg="#A7A7A7", fg="white", relief=SUNKEN, bd=1)
    entrerpseudo.place(relx=0.5, y=275, anchor="center")

    valider = PhotoImage(file="images/Valider.png")
    id_valider = zone_graphique.create_image(600, 400, anchor="c", image=valider)
    zone_graphique.tag_bind(id_valider, "<Button-1>", lambda event: ecran_jeu_bot())

    retour = PhotoImage(file="images/retour.png")
    id_retour = zone_graphique.create_image(1100, 550, anchor="c", image=retour)
    zone_graphique.tag_bind(id_retour, "<Button-1>", lambda event: accueil())

    pseudo2 = "Robot"

    return zone_graphique, entrerpseudo


def ecran_ami():
    global zone_graphique, fond_image, valider, retour, pseudo1, pseudo2, joueur, psdtour
    nettoyer_fenetre()
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=5, column=0, columnspan=3)

    fond_image = PhotoImage(file="images/fond.png")
    zone_graphique.create_image(600, 300, anchor="c", image=fond_image)

    titre = Label(fenetre, text="Pseudo du joueur 1", fg="white", bg='#5A5A5A', font="Arial 24 bold")
    titre.place(relx=0.5, y=150, anchor="center")

    entrerpseudo = Entry(fenetre, font=("Arial", 16), width=20, bg="#A7A7A7", fg="white", relief=SUNKEN, bd=1)
    entrerpseudo.place(relx=0.5, y=210, anchor="center")

    titre = Label(fenetre, text="Pseudo du joueur 2", fg="white", bg='#5A5A5A', font="Arial 24 bold")
    titre.place(relx=0.5, y=275, anchor="center")

    entrerpseudo2 = Entry(fenetre, font=("Arial", 16), width=20, bg="#A7A7A7", fg="white", relief=SUNKEN, bd=1)
    entrerpseudo2.place(relx=0.5, y=335, anchor="center")

    valider = PhotoImage(file="images/Valider.png")
    id_valider = zone_graphique.create_image(600, 435, anchor="c", image=valider)
    zone_graphique.tag_bind(id_valider, "<Button-1>", lambda event: ecran_jeu_ami())

    retour = PhotoImage(file="images/retour.png")
    id_retour = zone_graphique.create_image(1100, 550, anchor="c", image=retour)
    zone_graphique.tag_bind(id_retour, "<Button-1>", lambda event: accueil())

    pseudo2 = "Guillaume"

    return zone_graphique, entrerpseudo, valider, entrerpseudo2


def ecran_jeu_bot():
    # Zone et boosts
    global zone_graphique, boost1, boost2, boost3, boost12, boost22, boost33
    # Vies
    global logovie1, logovie2, logovie3, logovie4, logovie12, logovie22, logovie32, logovie42
    # Compteur de balles
    global fondballe, b1, b2, b3, b4, b5, b6, ordreclassique, jeu
    # Milieu
    global gundroite, f_gauche, f_droite, validationv, nbtour, inv1, inv2, validation, psdtour, vtour, joueur, bonus, id_validationv, id_fgauche, id_fdroite

    # global pseudo2

    nettoyer_fenetre()
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=10, column=0, columnspan=6)

    psdtour = pseudo1
    joueur = pseudo2

    tour = Label(fenetre, text=f"Tour {nbtour}", fg="white", bg='#272727', font="Arial 24")
    tour.place(relx=0.5, y=40, anchor="center")

    # Compteur de balles ---------------------------------------------------------------------------------------
    partie(vb, fb)

    fondballe = PhotoImage(file="images/fondballe.png")
    zone_graphique.create_image(600, 140, anchor="c", image=fondballe)

    # Balles blanches
    b1 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(525, 140, anchor="c", image=b1)
    b2 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(555, 140, anchor="c", image=b2)
    b3 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(585, 140, anchor="c", image=b3)
    b4 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(615, 140, anchor="c", image=b4)
    b5 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(645, 140, anchor="c", image=b5)
    b6 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(675, 140, anchor="c", image=b6)

    actualiser_balles()

    # Milieu ---------------------------------------------------------------------------------------
    vtour = Label(fenetre, text=f"Au tour de {psdtour}", fg="white", bg='#272727', font="Arial 24")
    vtour.place(relx=0.5, y=225, anchor="center")

    gundroite = PhotoImage(file="images/gun_droite.png")
    zone_graphique.create_image(600, 300, anchor="c", image=gundroite)

    f_gauche = PhotoImage(file="images/fgauche.png")
    id_fgauche = zone_graphique.create_image(500, 400, anchor="c", image=f_gauche)
    zone_graphique.tag_bind(id_fgauche, "<Button-1>", lambda event: tourner_gauche())

    f_droite = PhotoImage(file="images/fdroite.png")
    id_fdroite = zone_graphique.create_image(700, 400, anchor="c", image=f_droite)
    zone_graphique.tag_bind(id_fdroite, "<Button-1>", lambda event: tourner_droite())

    validation = Label(fenetre, text=f"Tirer sur {joueur} ?", fg="white", bg='#272727', font="Arial 24")
    validation.place(relx=0.5, y=475, anchor="center")

    validationv = PhotoImage(file="images/validation.png")
    id_validationv = zone_graphique.create_image(600, 540, anchor="c", image=validationv)
    zone_graphique.tag_bind(id_validationv, "<Button-1>", lambda event: etat_vie(joueur))

    # JOUEUR 1 ---------------------------------------------------------------------------------------
    psd1 = Label(fenetre, text=f"{pseudo1}", fg="white", bg='#272727', font="Arial 20 bold")
    psd1.place(x=85, y=30)

    # JOUEUR 1 VIE
    logovie1 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

    logovie2 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

    logovie3 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

    logovie4 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(180, 90, anchor="c", image=logovie4)

    # JOUEUR 1 BOOST
    boost1 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(125, 190, anchor="c", image=boost1)

    boost2 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(125, 340, anchor="c", image=boost2)

    boost3 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(125, 490, anchor="c", image=boost3)

    # Robot ---------------------------------------------------------------------------------------
    psd2 = Label(fenetre, text=f"{pseudo2}", fg="white", bg='#272727', font="Arial 20 bold")
    psd2.place(x=1030, y=30)

    # Robot VIE
    logovie12 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

    logovie22 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

    logovie32 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

    logovie42 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)

    # Robot BOOST
    boost12 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(1075, 190, anchor="c", image=boost12)

    boost22 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(1075, 340, anchor="c", image=boost22)

    boost33 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(1075, 490, anchor="c", image=boost33)

    # BOOSTS
    random_item(1)
    print(inv1, inv2)
    actualiser_bonus()

    return zone_graphique, nbtour


def ecran_jeu_ami():
    # Zone et boosts
    global zone_graphique, boost1, boost2, boost3, boost12, boost22, boost33
    # Vies
    global logovie1, logovie2, logovie3, logovie4, logovie12, logovie22, logovie32, logovie42
    # Compteur de balles
    global fondballe, b1, b2, b3, b4, b5, b6, ordreclassique, jeu
    # Milieu
    global gundroite, f_gauche, f_droite, validationv, nbtour, inv1, inv2, validation, psdtour, vtour, joueur, id_validationv

    nettoyer_fenetre()
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=10, column=0, columnspan=6)

    tourj = randint(0, 1)
    if tourj == 0:
        psdtour = pseudo1
        joueur = pseudo2
    else:
        psdtour = pseudo2
        joueur = pseudo1

    tour = Label(fenetre, text=f"Tour {nbtour}", fg="white", bg='#272727', font="Arial 24")
    tour.place(relx=0.5, y=40, anchor="center")

    # Compteur de balles ---------------------------------------------------------------------------------------
    partie(vb, fb)

    fondballe = PhotoImage(file="images/fondballe.png")
    zone_graphique.create_image(600, 140, anchor="c", image=fondballe)

    # Balles blanches
    b1 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(525, 140, anchor="c", image=b1)
    b2 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(555, 140, anchor="c", image=b2)
    b3 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(585, 140, anchor="c", image=b3)
    b4 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(615, 140, anchor="c", image=b4)
    b5 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(645, 140, anchor="c", image=b5)
    b6 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(675, 140, anchor="c", image=b6)

    actualiser_balles()

    # Milieu ---------------------------------------------------------------------------------------
    vtour = Label(fenetre, text=f"Au tour de {psdtour}", fg="white", bg='#272727', font="Arial 24")
    vtour.place(relx=0.5, y=225, anchor="center")

    gundroite = PhotoImage(file="images/gun_droite.png")
    zone_graphique.create_image(600, 300, anchor="c", image=gundroite)

    f_gauche = PhotoImage(file="images/fgauche.png")
    id_fgauche = zone_graphique.create_image(500, 400, anchor="c", image=f_gauche)
    zone_graphique.tag_bind(id_fgauche, "<Button-1>", lambda event: tourner_gauche())

    f_droite = PhotoImage(file="images/fdroite.png")
    id_fdroite = zone_graphique.create_image(700, 400, anchor="c", image=f_droite)
    zone_graphique.tag_bind(id_fdroite, "<Button-1>", lambda event: tourner_droite())

    validation = Label(fenetre, text=f"Tirer sur {joueur} ?", fg="white", bg='#272727', font="Arial 24")
    validation.place(relx=0.5, y=475, anchor="center")

    validationv = PhotoImage(file="images/validation.png")
    id_validationv = zone_graphique.create_image(600, 540, anchor="c", image=validationv)
    zone_graphique.tag_bind(id_validationv, "<Button-1>", lambda event: etat_vie(joueur))

    # JOUEUR 1 ---------------------------------------------------------------------------------------
    psd1 = Label(fenetre, text=f"{pseudo1}", fg="white", bg='#272727', font="Arial 20 bold")
    psd1.place(y=30)
    psd1.update_idletasks()
    text_width = psd1.winfo_reqwidth()
    psd1.place(x=125 - text_width // 2)

    # JOUEUR 1 VIE
    logovie1 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

    logovie2 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

    logovie3 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

    logovie4 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(180, 90, anchor="c", image=logovie4)

    # JOUEUR 1 BOOST
    boost1 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(125, 190, anchor="c", image=boost1)

    boost2 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(125, 340, anchor="c", image=boost2)

    boost3 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(125, 490, anchor="c", image=boost3)

    # JOUEUR 2 ---------------------------------------------------------------------------------------
    psd2 = Label(fenetre, text=f"{pseudo2}", fg="white", bg='#272727', font="Arial 20 bold")
    psd2.place(y=30)
    psd2.update_idletasks()
    text_width = psd2.winfo_reqwidth()
    psd2.place(x=1075 - text_width // 2)

    # JOUEUR 2 VIE
    logovie12 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

    logovie22 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

    logovie32 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

    logovie42 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)

    # JOUEUR 2 BOOST
    boost12 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(1075, 190, anchor="c", image=boost12)

    boost22 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(1075, 340, anchor="c", image=boost22)

    boost33 = PhotoImage(file="images/cercle_boost.png")
    zone_graphique.create_image(1075, 490, anchor="c", image=boost33)

    # BOOSTS
    random_item(1)
    print(inv1, inv2)
    actualiser_bonus()

    return zone_graphique, nbtour


def actualiser_balles():
    global zone_graphique, fondballe, b1, b2, b3, b4, b5, b6, ordreclassique, jeu, temp_balle_images

    tour = Label(fenetre, text=f"Tour {nbtour}", fg="white", bg='#272727', font="Arial 24")
    tour.place(relx=0.5, y=40, anchor="center")
    # Balles blanches
    b1 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(525, 140, anchor="c", image=b1)
    b2 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(555, 140, anchor="c", image=b2)
    b3 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(585, 140, anchor="c", image=b3)
    b4 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(615, 140, anchor="c", image=b4)
    b5 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(645, 140, anchor="c", image=b5)
    b6 = PhotoImage(file="images/blanc.png")
    zone_graphique.create_image(675, 140, anchor="c", image=b6)

    balles_images = {
        "vb": "images/rouge.png",
        "fb": "images/vert.png"
    }
    pos_balles = [(525, 140), (555, 140), (585, 140), (615, 140), (645, 140), (675, 140)]

    temp_balle_images = []

    i = 0
    for balle in ordreclassique:
        imgballe = balles_images.get(balle)
        if imgballe:
            img_balle = Image.open(imgballe)
            balle_image = ImageTk.PhotoImage(img_balle)
            zone_graphique.create_image(pos_balles[i][0], pos_balles[i][1], anchor="c", image=balle_image, tags="balle_image")
            temp_balle_images.append(balle_image)
            i = i + 1

    return temp_balle_images


def actualiser_bonus():
    global zone_graphique, inv1, inv2, temp_bonus_images1, temp_bonus_images2

    zone_graphique.delete("bonus_image")

    boosts_images = {
        "2damages": "images/bonus_degats.png",
        "bloquer": "images/bonus_rejouer.png",
        "vie": "images/bonus_vie.png",
        "voir": "images/bonus_balle.png",
        "skip": "images/bonus_vide.png"
    }

    pos_balles_1 = [(125, 175), (125, 325), (125, 475)]
    pos_balles_2 = [(1075, 175), (1075, 325), (1075, 475)]
    temp_bonus_images1 = []
    temp_bonus_images2 = []

    # Inventaire J1
    i = 0
    for bonus in inv1:
        img_bonus = boosts_images.get(bonus)
        if img_bonus:
            img = Image.open(img_bonus)
            img = ImageTk.PhotoImage(img)
            bonus_image = zone_graphique.create_image(125, pos_balles_1[i][1], anchor="c", image=img, tags="bonus_image")
            zone_graphique.tag_bind(bonus_image, "<Button-1>",
                                    lambda event, bonus=bonus, bonus_image=bonus_image: clique_bonus(event, bonus, bonus_image))
            temp_bonus_images1.append((img, bonus_image))
            i = i + 1

    # Inventaire J2
    i = 0
    for bonus in inv2:
        img_bonus = boosts_images.get(bonus)
        if img_bonus:
            img = Image.open(img_bonus)
            img = ImageTk.PhotoImage(img)
            bonus_image = zone_graphique.create_image(1075, pos_balles_2[i][1], anchor="c", image=img, tags="bonus_image")
            zone_graphique.tag_bind(bonus_image, "<Button-1>", lambda event, bonus=bonus, bonus_image=bonus_image: clique_bonus(event, bonus, bonus_image))
            temp_bonus_images2.append((img, bonus_image))
            i = i + 1

    return temp_bonus_images1, temp_bonus_images2


def clique_bonus(event, bonus, bonus_image):
    global zone_graphique, boost1, boost2, boost3, boost12, boost22, boost33, psdtour, inv1, inv2, x, pseudo1, pseudo2, utilisation, utilisationvoir, jeu, utilisationbloquer, rejouer1, rejouer2, ordreclassique
    x = event.x
    if len(jeu) > 0:
        if psdtour == pseudo1:
            if x > 600:
                print("Bonus joueur 2")
            elif x < 600:
                if bonus == "2damages":
                    if utilisation == 0:
                        utilisation = utilisation + 1
                        double_degats(pseudo1)
                        zone_graphique.delete(bonus_image)
                        print("Damages x2")
                    elif utilisation >= 1:
                        print("Tu ne peux pas utiliser")
                elif bonus == "bloquer":
                    if utilisationbloquer == 0:
                        utilisationbloquer = utilisationbloquer + 1
                        zone_graphique.delete(bonus_image)
                        rejouer_bonus(pseudo1)
                        print("Bloquer")
                    elif utilisationbloquer >= 1:
                        print("Tu ne peux pas utiliser")
                elif bonus == "vie":
                    if vie1 < 4:
                        zone_graphique.delete(bonus_image)
                        reprendrevie(pseudo1)
                    elif vie1 == 4:
                        print("Tu as le maximum de vie")
                    actualiser_vie()
                    print(inv1)
                elif bonus == "voir":
                    if utilisationvoir == 0:
                        utilisationvoir = utilisationvoir + 1
                        zone_graphique.delete(bonus_image)
                        prochaine_balle(pseudo1)
                        print("Voir")
                    elif utilisationvoir >= 1:
                        print("Tu ne peux pas utiliser")
                elif bonus == "skip":
                    zone_graphique.delete(bonus_image)
                    tirer_vide(pseudo1)
                    print("Skip")
        elif psdtour == pseudo2:
            if x < 600:
                print("Bonus joueur 1")
            elif x > 600:
                if bonus == "2damages":
                    if utilisation == 0:
                        utilisation = utilisation + 1
                        double_degats(pseudo2)
                        zone_graphique.delete(bonus_image)
                        print("Damages x2")
                    elif utilisation >= 1:
                        print("Tu ne peux pas utiliser")
                elif bonus == "bloquer":
                    if utilisationbloquer == 0:
                        utilisationbloquer = utilisationbloquer + 1
                        zone_graphique.delete(bonus_image)
                        rejouer_bonus(pseudo2)
                        print("Bloquer")
                    elif utilisationbloquer >= 1:
                        print("Tu ne peux pas utiliser")
                elif bonus == "vie":
                    if vie2 < 4:
                        zone_graphique.delete(bonus_image)
                        reprendrevie(pseudo2)
                    elif vie2 == 4:
                        print("Tu as le maximum de vie")
                    actualiser_vie()
                    print(inv2)
                elif bonus == "voir":
                    if utilisationvoir == 0:
                        utilisationvoir = utilisationvoir + 1
                        zone_graphique.delete(bonus_image)
                        prochaine_balle(pseudo2)
                        print("Voir")
                    elif utilisationvoir >= 1:
                        print("Tu ne peux pas utiliser")
                elif bonus == "skip":
                    zone_graphique.delete(bonus_image)
                    tirer_vide(pseudo2)
                    print("Skip")
    elif len(jeu) == 0:
        print("Fin du round : tu ne peux pas utiliser ça")


def tourner_gauche():
    global zone_graphique, gundroite, gungauche, joueur
    zone_graphique.delete(gundroite)

    gungauche = PhotoImage(file="images/gun_gauche.png")

    gundegauche = zone_graphique.create_image(600, 300, anchor="c", image=gungauche)
    joueur = pseudo1
    gundroite = gundegauche
    validation.config(text=f"Tirer sur {joueur} ?")


def tourner_droite():
    global zone_graphique, gundroite, gungauche, gundegauche, joueur
    zone_graphique.delete(gundroite)

    gundroite = PhotoImage(file="images/gun_droite.png")

    gundedroite = zone_graphique.create_image(600, 300, anchor="c", image=gundroite)
    joueur = pseudo2
    gungauche = gundedroite
    validation.config(text=f"Tirer sur {joueur} ?")


def etat_vie(joueur):
    global zone_graphique, logovie1, logovie2, logovie3, logovie4, logovie12, logovie22, logovie32, logovie42, vie1, vie2, jeu, utilisation, ordreclassique, nbtour, inv1, inv2, degatsx2, psdtour, vtour, validationv, cachevalider, ballesuivante, balleapres, utilisationvoir, utilisationbloquer, rejouer1, rejouer2, gagnant, victoire, bonus, id_validationv, id_fgauche, id_fdroite
    if len(jeu) - 1 == 0:
        if balleapres == True:
            balleapres = False
            ballesuivante.destroy()
        for i in jeu:
            utilisation = 0
            utilisationvoir = 0
            utilisationbloquer = 0
            if i == "fb":
                if degatsx2 == True:
                    degatsx2 = False
                PlaySound("fb.wav", SND_ASYNC)
                del ordreclassique[-1]
                del jeu[0]
                actualiser_balles()
                if joueur == pseudo1:
                    print("Fausse balle joueur 1")
                    if psdtour == pseudo1 or rejouer1 == True:
                        psdtour = pseudo1
                        rejouer1 = False
                        if pseudo2 == "Robot":
                            commandesjoueur()
                    elif psdtour == pseudo2:
                        if rejouer2 == True:
                            psdtour = pseudo2
                            rejouer2 = False
                            botjoue()
                        else:
                            psdtour = pseudo1
                            if pseudo2 == "Robot":
                                commandesjoueur()
                elif joueur == pseudo2:
                    print("Fausse balle joueur 2")
                    if psdtour == pseudo2 or rejouer2 == True:
                        psdtour = pseudo2
                        rejouer2 = False
                        botjoue()
                    elif psdtour == pseudo1:
                        if rejouer1 == True:
                            psdtour = pseudo1
                            rejouer1 = False
                            if pseudo2 == "Robot":
                                commandesjoueur()
                        else:
                            psdtour = pseudo2
                            botjoue()
                vtour.config(text=f"Au tour de {psdtour}")
            elif i == "vb":
                if degatsx2 == True:
                    if joueur == pseudo1:
                        vie1 = vie1 - 1
                        degatsx2 = False
                        PlaySound("bruitx2.wav", SND_ASYNC)
                        if vie1 == 0:
                            victoire = True
                            gagnant = pseudo2
                            ecran_fin()
                        elif vie2 == 0:
                            victoire = True
                            gagnant = pseudo1
                            ecran_fin()
                        else:
                            actualiser_vie()
                    elif joueur == pseudo2:
                        vie2 = vie2 - 1
                        degatsx2 = False
                        PlaySound("bruitx2.wav", SND_ASYNC)
                        if vie1 == 0:
                            victoire = True
                            gagnant = pseudo2
                            ecran_fin()
                        elif vie2 == 0:
                            victoire = True
                            gagnant = pseudo1
                            ecran_fin()
                        else:
                            actualiser_vie()
                else:
                    PlaySound("tir.wav", SND_ASYNC)
                del ordreclassique[0]
                del jeu[0]
                actualiser_balles()
                if joueur == pseudo1:
                    print("Vraie balle joueur 1")
                    vie1 = vie1 - 1
                    if psdtour == pseudo2 or rejouer2 == True:
                        psdtour = pseudo2
                        rejouer2 = False
                        botjoue()
                    elif psdtour == pseudo1:
                        if rejouer1 == True:
                            psdtour = pseudo1
                            rejouer1 = False
                            if pseudo2 == "Robot":
                                commandesjoueur()
                        else:
                            psdtour = pseudo2
                            botjoue()
                    vtour.config(text=f"Au tour de {psdtour}")
                    if vie1 == 0:
                        victoire = True
                        gagnant = pseudo2
                        ecran_fin()
                    elif vie2 == 0:
                        victoire = True
                        gagnant = pseudo1
                        ecran_fin()
                    else:
                        actualiser_vie()
                        
                elif joueur == pseudo2:
                    print("Vraie balle joueur 2")
                    vie2 = vie2 - 1
                    if psdtour == pseudo1 or rejouer1 == True:
                        psdtour = pseudo1
                        rejouer1 = False
                        if pseudo2 == "Robot":
                            commandesjoueur()
                    elif psdtour == pseudo2:
                        if rejouer2 == True:
                            psdtour = pseudo2
                            rejouer2 = False
                            botjoue()
                        else:
                            psdtour = pseudo1
                            if pseudo2 == "Robot":
                                commandesjoueur()
                    vtour.config(text=f"Au tour de {psdtour}")
                    if vie1 == 0:
                        victoire = True
                        gagnant = pseudo2
                        ecran_fin()
                    elif vie2 == 0:
                        victoire = True
                        gagnant = pseudo1
                        ecran_fin()
                    else:
                        actualiser_vie()
        actualiser_balles()
        nbtour = nbtour + 1
        time.sleep(0.5)
        PlaySound("newround.wav", SND_ASYNC)
        toursuivant()
    else:
        if balleapres == True:
            balleapres = False
            ballesuivante.destroy()
        for i in jeu:
            utilisation = 0
            utilisationvoir = 0
            utilisationbloquer = 0
            if i == "fb":
                if degatsx2 == True:
                    degatsx2 = False
                PlaySound("fb.wav", SND_ASYNC)
                del ordreclassique[-1]
                del jeu[0]
                actualiser_balles()
                if joueur == pseudo1:
                    print("Fausse balle joueur 1")
                    if psdtour == pseudo1 or rejouer1 == True:
                        psdtour = pseudo1
                        rejouer1 = False
                        if pseudo2 == "Robot":
                            commandesjoueur()
                    elif psdtour == pseudo2:
                        if rejouer2 == True:
                            psdtour = pseudo2
                            rejouer2 = False
                            botjoue()
                        else:
                            psdtour = pseudo1
                            if pseudo2 == "Robot":
                                commandesjoueur()
                elif joueur == pseudo2:
                    print("Fausse balle joueur 2")
                    if psdtour == pseudo2 or rejouer2 == True:
                        psdtour = pseudo2
                        rejouer2 = False
                        botjoue()
                    elif psdtour == pseudo1:
                        if rejouer1 == True:
                            psdtour = pseudo1
                            rejouer1 = False
                            if pseudo2 == "Robot":
                                commandesjoueur()
                        else:
                            psdtour = pseudo2
                            botjoue()
                vtour.config(text=f"Au tour de {psdtour}")
                break
            elif i == "vb":
                if degatsx2 == True:
                    if joueur == pseudo1:
                        vie1 = vie1 - 1
                        degatsx2 = False
                        PlaySound("bruitx2.wav", SND_ASYNC)
                        if vie1 == 0:
                            victoire = True
                            gagnant = pseudo2
                            ecran_fin()
                        elif vie2 == 0:
                            victoire = True
                            gagnant = pseudo1
                            ecran_fin()
                        else:
                            actualiser_vie()
                    elif joueur == pseudo2:
                        vie2 = vie2 - 1
                        degatsx2 = False
                        PlaySound("bruitx2.wav", SND_ASYNC)
                        if vie1 == 0:
                            victoire = True
                            gagnant = pseudo2
                            ecran_fin()
                        elif vie2 == 0:
                            victoire = True
                            gagnant = pseudo1
                            ecran_fin()
                        else:
                            actualiser_vie()
                else:
                    PlaySound("tir.wav", SND_ASYNC)
                del ordreclassique[0]
                del jeu[0]
                actualiser_balles()
                if joueur == pseudo1:
                    print("Vraie balle joueur 1")
                    vie1 = vie1 - 1
                    if psdtour == pseudo2 or rejouer2 == True:
                        psdtour = pseudo2
                        rejouer2 = False
                        botjoue()
                    elif psdtour == pseudo1:
                        if rejouer1 == True:
                            psdtour = pseudo1
                            rejouer1 = False
                            if pseudo2 == "Robot":
                                commandesjoueur()
                        else:
                            psdtour = pseudo2
                            botjoue()
                    vtour.config(text=f"Au tour de {psdtour}")
                    if vie1 == 0:
                        victoire = True
                        gagnant = pseudo2
                        ecran_fin()
                    elif vie2 == 0:
                        victoire = True
                        gagnant = pseudo1
                        ecran_fin()
                    else:
                        actualiser_vie()
                        break
                elif joueur == pseudo2:
                    print("Vraie balle joueur 2")
                    vie2 = vie2 - 1
                    if psdtour == pseudo1 or rejouer1 == True:
                        psdtour = pseudo1
                        rejouer1 = False
                        if pseudo2 == "Robot":
                            commandesjoueur()
                    elif psdtour == pseudo2:
                        if rejouer2 == True:
                            psdtour = pseudo2
                            rejouer2 = False
                            botjoue()
                        else:
                            psdtour = pseudo1
                    vtour.config(text=f"Au tour de {psdtour}")
                    if vie1 == 0:
                        victoire = True
                        gagnant = pseudo2
                        ecran_fin()
                    elif vie2 == 0:
                        victoire = True
                        gagnant = pseudo1
                        ecran_fin()
                    else:
                        actualiser_vie()
                        break
                    
            return zone_graphique, nbtour


def botjoue():
    global zone_graphique, fenetre, psdtour, bottour, id_fgauche, id_fdroite, id_validationv, pseudo1, pseudo2, lebotjoue, validation
    print(psdtour)
    if pseudo2 == "Robot":
        if psdtour == "Robot":
            zone_graphique.tag_unbind(id_fgauche, "<Button-1>")
            zone_graphique.tag_unbind(id_fdroite, "<Button-1>")
            zone_graphique.delete(id_validationv)
            lebotjoue = Label(fenetre, text=f"Le bot joue...", fg="white", bg='#272727', font="Arial 24 bold")
            lebotjoue.place(relx=0.5, y=535, anchor="center")
            while psdtour == "Robot":
                actualiser_balles()
                actualiser_vie()
                vtour.config(text=f"Au tour de {psdtour}")
                rdmbottir = randint(0, 1)
                if rdmbottir == 0:
                    tourner_gauche()
                    zone_graphique.update()
                    validation.config(text=f"Le bot tire sur {joueur}")
                    time.sleep(1)
                    etat_vie(pseudo1)
                else:
                    tourner_droite()
                    zone_graphique.update()
                    validation.config(text=f"Le bot tire sur {joueur}")
                    time.sleep(1)
                    etat_vie(pseudo2)
                lebotjoue.destroy()
                if len(jeu) == 0:
                    print("Fin du round")
                    lebotjoue.destroy()
                    break
            psdtour = pseudo1
        elif psdtour == pseudo1:
            commandesjoueur()
    return zone_graphique


def commandesjoueur():
    global zone_graphique, fenetre, psdtour, bottour, id_fgauche, id_fdroite, id_validationv, pseudo1, pseudo2, validation, validationv, lebotjoue, vtour
    print("test")
    try:
        lebotjoue.destroy()
    except:
        print("pas marché")
        pass
    finally:
        vtour.config(text=f"Au tour de {psdtour}")
        zone_graphique.tag_bind(id_fgauche, "<Button-1>", lambda event: tourner_gauche())
        zone_graphique.tag_bind(id_fdroite, "<Button-1>", lambda event: tourner_droite())

        validation.config(text=f"Tirer sur {joueur} ?")

        id_validationv = zone_graphique.create_image(600, 540, anchor="c", image=validationv)
        zone_graphique.tag_bind(id_validationv, "<Button-1>", lambda event: etat_vie(joueur))
        print("testbouton")
        zone_graphique.update()
    return zone_graphique
    

def toursuivant():
    global zone_graphique, nbtour, vie1, vie2, pseudo1, pseudo2, victoire, gagnant
    if nbtour == 2:
        if vie1 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie2 == 0:
            victoire = True
            gagnant = pseudo1
            ecran_fin()
        else:
            print("2eme round")
            vb = 3
            fb = 2
            random_item(2)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
            botjoue()
    if nbtour == 3:
        if vie1 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie2 == 0:
            victoire = True
            gagnant = pseudo1
            ecran_fin()
        else:
            print("3eme round")
            vb = 3
            fb = 3
            random_item(1)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
            botjoue()
    if nbtour == 4:
        if vie1 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie2 == 0:
            victoire = True
            gagnant = pseudo1
            ecran_fin()
        else:
            print("4eme round")
            vb = 2
            fb = 4
            random_item(2)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
            botjoue()
    if nbtour == 5:
        if vie1 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie2 == 0:
            victoire = True
            gagnant = pseudo1
            ecran_fin()
        else:
            print("5eme round")
            vb = 1
            fb = 5
            random_item(3)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
            botjoue()
    if nbtour == 6:
        if vie1 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie2 == 0:
            victoire = True
            gagnant = pseudo1
            ecran_fin()
        else:
            print("6eme round")
            vb = 4
            fb = 2
            random_item(3)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
            botjoue()
    if nbtour == 7:
        if vie1 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie2 == 0:
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie1 > vie2:
            print("Le joueur 1 a gagné car le joueur 2 avait moins de vie")
            victoire = True
            gagnant = pseudo1
            ecran_fin()
        elif vie2 > vie1:
            print("Le joueur 2 a gagné car le joueur 1 avait moins de vie")
            victoire = True
            gagnant = pseudo2
            ecran_fin()
        elif vie1 == vie2:
            print("Égalitée")
            victoire = False
            ecran_fin()


def actualiser_vie():
    global zone_graphique, logovie1, logovie2, logovie3, logovie4, logovie12, logovie22, logovie32, logovie42, vie1, vie2, jeu, utilisation, ordreclassique, nbtour, inv1, inv2, degatsx2, psdtour, vtour, validationv, cachevalider, victoire, gagnant
    if vie1 == 4:
        logovie1 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

        logovie2 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

        logovie3 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

        logovie4 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(180, 90, anchor="c", image=logovie4)
    if vie1 == 3:
        logovie1 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

        logovie2 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

        logovie3 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

        logovie4 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(180, 90, anchor="c", image=logovie4)
    if vie1 == 2:
        logovie1 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

        logovie2 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

        logovie3 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

        logovie4 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(180, 90, anchor="c", image=logovie4)
    if vie1 == 1:
        logovie1 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

        logovie2 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

        logovie3 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

        logovie4 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(180, 90, anchor="c", image=logovie4)
    if vie1 <= 0:
        logovie1 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(75, 90, anchor="c", image=logovie1)

        logovie2 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(110, 90, anchor="c", image=logovie2)

        logovie3 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(145, 90, anchor="c", image=logovie3)

        logovie4 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(180, 90, anchor="c", image=logovie4)
        print("Joueur 1 a perdu")
        vie1 = 0
        victoire = True
        gagnant = pseudo2
        ecran_fin()

    if vie2 == 4:
        logovie12 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

        logovie22 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

        logovie32 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

        logovie42 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)
    if vie2 == 3:
        logovie12 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

        logovie22 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

        logovie32 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

        logovie42 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)
    if vie2 == 2:
        logovie12 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

        logovie22 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

        logovie32 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

        logovie42 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)
    if vie2 == 1:
        logovie12 = PhotoImage(file="images/blanc.png")
        zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

        logovie22 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

        logovie32 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

        logovie42 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)
    if vie2 <= 0:
        logovie12 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1020, 90, anchor="c", image=logovie12)

        logovie22 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1055, 90, anchor="c", image=logovie22)

        logovie32 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1090, 90, anchor="c", image=logovie32)

        logovie42 = PhotoImage(file="images/gris.png")
        zone_graphique.create_image(1125, 90, anchor="c", image=logovie42)
        print("Joueur 2 a perdu")
        vie2 = 0
        victoire = True
        gagnant = pseudo1
        ecran_fin()


def partie(vb, fb):
    global vie1, vie2, ordreclassique, jeu
    nb_balle = vb + fb
    ordre = []
    jeu = []
    ordreclassique = []
    for a in range(nb_balle):
        jeu.append(".")
    ordre = liste(nb_balle)
    for i in range(vb):
        nb = ordre[i] - 1
        ordreclassique.append("vb")
        jeu[nb] = "vb"
    for j in range(len(jeu)):
        if jeu[j] == ".":
            jeu[j] = "fb"
            ordreclassique.append("fb")
    print(jeu)
    return jeu, ordreclassique


def ordre():
    global ordreclassique, jeu
    ordreclassique = []
    for balle in jeu:
        if balle == "fb":
            ordreclassique.append("fb")
        elif balle == "vb":
            ordreclassique.insert(0, "vb")
    return ordreclassique


def liste(nb_balle):
    liste = []
    while len(liste) != nb_balle:
        rdm = randint(1, nb_balle)
        if rdm in liste:
            rdm = randint(1, nb_balle)
        else:
            liste.append(rdm)
    return liste


def random_item(nombre_item):
    inv1.clear()
    inv2.clear()
    for i in range(nombre_item):
        rdm = randint(0, 4)
        inv1.append(item[rdm])
        rdm = randint(0, 4)
        inv2.append(item[rdm])


def reprendrevie(joueur):
    global zone_graphique, vie1, vie2, inv1, inv2
    n = 0
    print(vie1, vie2)
    if joueur == pseudo1:
        if vie1 >= 4:
            print("Tu ne peux pas utiliser ça")
        else:
            vie1 = vie1 + 1
            print(vie1, vie2)
            for i in inv1:
                n = n + 1
                if i == "vie":
                    del inv1[n - 1]
                    break
    elif joueur == pseudo2:
        if vie2 >= 4:
            print("Tu ne peux pas utiliser ça")
        else:
            vie2 = vie2 + 1
            print(vie1, vie2)
            for i in inv2:
                n = n + 1
                if i == "vie":
                    del inv2[n - 1]
                    break


def double_degats(joueur):
    global vie1, vie2, inv1, inv2, degatsx2
    n = 0
    degatsx2 = True
    if joueur == pseudo1:
        for i in inv1:
            n = n + 1
            if i == "2damages":
                del inv1[n - 1]
                break
    if joueur == pseudo2:
        for i in inv2:
            n = n + 1
            if i == "2damages":
                del inv2[n - 1]
                break


def prochaine_balle(joueur):
    global jeu, ordreclassique, inv1, inv2, zone_graphique, ballesuivante, balleapres
    n = 0
    balleapres = True
    if joueur == pseudo1:
        if jeu[0] == "fb":
            ballesuivante = Label(fenetre, text=f"Balle actuelle : fausse balle", fg="white", bg='#272727',
                                  font="Arial 14")
            ballesuivante.place(x=350, y=100, anchor="center")
        elif jeu[0] == "vb":
            ballesuivante = Label(fenetre, text=f"Balle actuelle : vraie balle", fg="white", bg='#272727',
                                  font="Arial 14")
            ballesuivante.place(x=350, y=100, anchor="center")
        for i in inv1:
            n = n + 1
            if i == "voir":
                del inv1[n - 1]
                print("1", inv1, inv2)
                break
    elif joueur == pseudo2:
        if jeu[0] == "fb":
            ballesuivante = Label(fenetre, text=f"Balle actuelle : fausse balle", fg="white", bg='#272727',
                                  font="Arial 14")
            ballesuivante.place(x=850, y=100, anchor="center")
        elif jeu[0] == "vb":
            ballesuivante = Label(fenetre, text=f"Balle actuelle : vraie balle", fg="white", bg='#272727',
                                  font="Arial 14")
            ballesuivante.place(x=850, y=100, anchor="center")
        for i in inv2:
            n = n + 1
            if i == "voir":
                del inv2[n - 1]
                print("2", inv1, inv2)
                break


def tirer_vide(joueur):
    global jeu, ordreclassique, inv1, inv2, zone_graphique, nbtour
    n = 0
    if len(jeu) - 1 == 0:
        del jeu[0]
        ordre()
        nbtour = nbtour + 1
        time.sleep(0.5)
        PlaySound("newround.wav", SND_ASYNC)
        if nbtour == 2:
            print("2eme round")
            vb = 3
            fb = 2
            random_item(2)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
        if nbtour == 3:
            print("3eme round")
            vb = 3
            fb = 3
            random_item(1)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
        if nbtour == 4:
            print("4eme round")
            vb = 2
            fb = 4
            random_item(2)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
        if nbtour == 5:
            print("5eme round")
            vb = 1
            fb = 5
            random_item(3)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
        if nbtour == 6:
            print("6eme round")
            vb = 4
            fb = 2
            random_item(3)
            actualiser_bonus()
            print(inv1, inv2)
            partie(vb, fb)
            actualiser_balles()
        if joueur == pseudo1:
            for i in inv1:
                n = n + 1
                if i == "skip":
                    del inv1[n - 1]
                    break
        if joueur == pseudo2:
            for i in inv2:
                n = n + 1
                if i == "skip":
                    del inv2[n - 1]
                    break
    else:
        del jeu[0]
        ordre()
        actualiser_balles()
        if joueur == pseudo1:
            for i in inv1:
                n = n + 1
                if i == "skip":
                    del inv1[n - 1]
                    break
        if joueur == pseudo2:
            for i in inv2:
                n = n + 1
                if i == "skip":
                    del inv2[n - 1]
                    break


def rejouer_bonus(joueur):
    global jeu, ordreclassique, inv1, inv2, zone_graphique, rejouer1, rejouer2
    n = 0
    if joueur == pseudo1:
        rejouer1 = True
        for i in inv1:
            n = n + 1
            if i == "bloquer":
                del inv1[n - 1]
                break
    if joueur == pseudo2:
        rejouer2 = True
        for i in inv2:
            n = n + 1
            if i == "bloquer":
                del inv2[n - 1]
                break


def ecran_fin():
    global zone_graphique, fond_image, valider, retour, pseudo1, pseudo2, joueur, gagnant, victoire, ordreclassique, inv1, inv2
    nettoyer_fenetre()
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=5, column=0, columnspan=3)

    fond_image = PhotoImage(file="images/fond.png")
    zone_graphique.create_image(600, 300, anchor="c", image=fond_image)

    if victoire == True:
        victoire = False
        titre = Label(fenetre, text=f"Victoire de {gagnant} ♕", fg="white", bg='#5A5A5A', font="Arial 24 bold")
        titre.place(relx=0.5, y=175, anchor="center")

        viej1 = Label(fenetre, text=f"{pseudo1} : {vie1} vie(s)", fg="white", bg='#5A5A5A', font="Arial 24")
        viej1.place(relx=0.5, y=250, anchor="center")

        viej2 = Label(fenetre, text=f"{pseudo2} : {vie2} vie(s)", fg="white", bg='#5A5A5A', font="Arial 24")
        viej2.place(relx=0.5, y=325, anchor="center")


    else:
        titre = Label(fenetre, text=f"Égalitée", fg="white", bg='#5A5A5A', font="Arial 24 bold")
        titre.place(relx=0.5, y=175, anchor="center")

        viej1 = Label(fenetre, text=f"{pseudo1} : {vie1} vie(s)", fg="white", bg='#5A5A5A', font="Arial 24")
        viej1.place(relx=0.5, y=250, anchor="center")

        viej2 = Label(fenetre, text=f"{pseudo2} : {vie2} vie(s)", fg="white", bg='#5A5A5A', font="Arial 24")
        viej2.place(relx=0.5, y=325, anchor="center")

    retour = PhotoImage(file="images/retour.png")
    id_retour = zone_graphique.create_image(1100, 550, anchor="c", image=retour)
    zone_graphique.tag_bind(id_retour, "<Button-1>", lambda event: accueil())

    return zone_graphique


def comment_jouer():
    global zone_graphique, compteur, bonustout, retour

    nettoyer_fenetre()
    zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
    zone_graphique.grid(row=0, rowspan=10, column=0, columnspan=6)

    desc = Label(fenetre, text="Chaque joueur commence avec 4 vies qui sont représentées en"
                               "\nboulles blanches sous son pseudo. Il peut y avoir jusqu'à 6 balles sur le compteur."
                               "\nLes boules blanches indiquent le nombre total de balles. Les boules rouges"
                               "\nsont réelles et les vertes sont fausses. Les joueurs peuvent viser"
                               "\nsois eux-mêmes sois leur adversaire. L'objectif est d'épuiser les vies"
                               "\nde l'adversaire."
                               "\n\nPendant le jeu, les joueurs peuvent obtenir différents"
                               "\nbonus : un coeur pour récupérer une vie (le maximum est 4), les doubles flèches pour jouer deux fois,"
                               "\nun point d'interrogation pour connaître la prochaine balle, une explosion"
                               "\npour doubler les dégâts, et un pistolet pour tirer une balle vide.",
                 fg="white", bg='#272727', font="Arial 14")
    desc.place(x=450, y=150, anchor="center")

    compteur = PhotoImage(file="images/compteur.png")
    zone_graphique.create_image(1050, 100, anchor="c", image=compteur)

    bonusliste = Label(fenetre, text="Liste des bonus :", fg="white", bg='#272727', font="Arial 14")
    bonusliste.place(x=100, y=350, anchor="center")

    bonustout = PhotoImage(file="images/bonustout.png")
    zone_graphique.create_image(450, 450, anchor="c", image=bonustout)

    retour = PhotoImage(file="images/retour.png")
    id_retour = zone_graphique.create_image(1100, 550, anchor="c", image=retour)
    zone_graphique.tag_bind(id_retour, "<Button-1>", lambda event: accueil())


# Variables globales ------------------------------------------------------

nbtour = 1
pseudo1 = "Oscar"
vie1 = 4
vie2 = 4
vb = 1
fb = 2
degatsx2 = False
balleapres = False
rejouer1 = False
rejouer2 = False
bottour = False
item = ["2damages", "bloquer", "vie", "voir", "skip"]
inv1 = []
inv2 = []
utilisation = 0
utilisationvoir = 0
utilisationbloquer = 0

# Main --------------------------------------------------------------------

fenetre = creer_fenetre()
zone_graphique = Canvas(fenetre, width=1200, height=600, bg='#272727')
zone_graphique, titre, bouton_1, bouton_2, bouton_3 = accueil()

fenetre.mainloop()
