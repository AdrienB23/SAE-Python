from upemtk import *
from random import *
from time import *
from math import *
import os
import json

liste_cercle_1 = []
liste_cercle_2 = []

fichier = "config.txt"
fi = open(fichier)
config = []
for lignes in fi:
    if lignes[len(lignes)-1] == "\n":
        config.append(lignes[:-1])
    else:
        config.append(lignes)
fi.close()     
for i in range(len(config)):
    config[i] = config[i].split(":")

largeur_fenetre = int(config[0][-1])
hauteur_fenetre = int(config[1][-1])
coef_largeur = largeur_fenetre/1280
coef_hauteur = hauteur_fenetre/720

couleurJoueur = [config[3][-1].strip(), config[4][-1].strip()]

epargne_1 = int(config[6][-1])
epargne_2 = int(config[6][-1])

liste_variables = ["liste_cercle_1", "liste_cercle_2", "tour", "numero_tour", "nb_max_tour", "epargne_1", "epargne_2"]

######################## Fonction d'aspect graphique des différents affichages ###################################################

def fond_sauvegarde():
    rectangle(int(2*coef_largeur), int(2*coef_hauteur), int(1277*coef_largeur), int(150*coef_hauteur), "white", epaisseur=5, tag="Sauvegarde")
    texte(int(640*coef_largeur), int(75*coef_hauteur), "Choisissez une sauvegarde", "white", "center", taille=int(50*coef_hauteur), tag="Sauvegarde")

    rectangle(int(440*coef_largeur), int(200*coef_hauteur), int(840*coef_largeur), int(300*coef_hauteur), "white", "#009382", 5, tag="Sauvegarde")
    texte(int(640*coef_largeur), int(250*coef_hauteur), "Sauvegarde 1", "white", "center", taille=int(40*coef_hauteur), tag="Sauvegarde")

    rectangle(int(440*coef_largeur), int(350*coef_hauteur), int(840*coef_largeur), int(450*coef_hauteur), "white", "#009382", 5, tag="Sauvegarde")
    texte(int(640*coef_largeur), int(400*coef_hauteur), "Sauvegarde 2", "white", "center", taille=int(40*coef_hauteur), tag="Sauvegarde")

    rectangle(int(440*coef_largeur), int(500*coef_hauteur),int(840*coef_largeur), int(600*coef_hauteur), "white", "#009382", 5, tag="Sauvegarde")
    texte(int(640*coef_largeur),int(550*coef_hauteur),"Sauvegarde 3", "white", "center", taille=int(40*coef_hauteur), tag="Sauvegarde")
    mise_a_jour()

def fond_menu(): # Affiche le menu du jeu
    rectangle(int(2*coef_largeur), int(2*coef_hauteur), int(1277*coef_largeur), int(150*coef_hauteur), "white", epaisseur=5, tag="Menu")
    texte(int(640*coef_largeur), int(75*coef_hauteur), "Bataille des boules", "white", "center", taille=int(50*coef_hauteur), tag="Menu")

    rectangle(int(200*coef_largeur), int(300*coef_hauteur), int(600*coef_largeur), int(400*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(400*coef_largeur), int(350*coef_hauteur), "Jouer", "white", "center", taille=int(40*coef_hauteur), tag="Menu")

    rectangle(int(650*coef_largeur), int(300*coef_hauteur), int(1050*coef_largeur), int(400*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(850*coef_largeur), int(350*coef_hauteur), "Charger Sauv.", "white", "center", taille=int(40*coef_hauteur), tag="Menu")

    rectangle(int(200*coef_largeur), int(450*coef_hauteur), int(600*coef_largeur), int(550*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(400*coef_largeur), int(500*coef_hauteur), "Variantes", "white", "center", taille=int(40*coef_hauteur), tag="Menu")

    rectangle(int(650*coef_largeur), int(450*coef_hauteur),int(1050*coef_largeur), int(550*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(850*coef_largeur),int(500*coef_hauteur),"Quitter", "white", "center", taille=int(40*coef_hauteur), tag="Menu")
    mise_a_jour()

def fond_jeu(): # Affiche les éléments du terrains de jeu
    rectangle(int(50*coef_largeur), int(100*coef_hauteur), int(1230*coef_largeur), int(670*coef_hauteur), "floralwhite","floralwhite", tag="Jeu")

    rectangle(int(1130*coef_largeur), int(680*coef_hauteur), int(1230*coef_largeur), int(715*coef_hauteur), "black","red", 1, "Retour Jeu")
    texte(int(1180*coef_largeur), int(698*coef_hauteur), "Retour", "white", "c", taille=int(16*coef_hauteur), tag="Retour Jeu")
    mise_a_jour()

def variantes(Sablier, Scores, Taille, Dynamique, Terminaison, Obstacle): # Affiche le menu des variantes pour choisir une ou plusieurs variantes (pour l'instant seul le sablier est disponible)
    efface("Variante")
    rectangle(int(2*coef_largeur),int(2*coef_hauteur), int(1277*coef_largeur), int(150*coef_hauteur), "white", epaisseur=5, tag="Variante")
    texte(int(640*coef_largeur), int(75*coef_hauteur), "Variantes", "white", "center", taille=int(50*coef_hauteur), tag="Variante")
    if Sablier:
        rectangle(int(275*coef_largeur), int(200*coef_hauteur), int( 575*coef_largeur), int(300*coef_hauteur), "white", "green", 5, tag="Variante Sablier")
        texte(int(425*coef_largeur), int(250*coef_hauteur), "Sablier", "white", "center", taille=int(32*coef_hauteur), tag="Variante Sablier")
    else:
        rectangle(int(275*coef_largeur), int(200*coef_hauteur), int( 575*coef_largeur), int(300*coef_hauteur), "white", "red", 5, tag="Variante Sablier")
        texte(int(425*coef_largeur), int(250*coef_hauteur), "Sablier", "white", "center", taille=int(32*coef_hauteur), tag="Variante Sablier")
    if Scores:
        rectangle(int(625*coef_largeur), int(200*coef_hauteur), int( 925*coef_largeur), int(300*coef_hauteur), "white", "green", 5, tag="Variante Scores")
        texte(int(775*coef_largeur), int(250*coef_hauteur), "Scores", "white", "center", taille=int(32*coef_hauteur), tag="Variante Scores" )
    else:
        rectangle(int(625*coef_largeur), int(200*coef_hauteur),int( 925*coef_largeur), int(300*coef_hauteur), "white", "red", 5, tag="Variante Scores")
        texte(int(775*coef_largeur), int(250*coef_hauteur),"Scores", "white", "center", taille=int(32*coef_hauteur), tag="Variante Scores" )
    if Taille:
        rectangle(int(275*coef_largeur), int(350*coef_hauteur),int( 575*coef_largeur), int(450*coef_hauteur), "white", "green", 5, tag="Variante Taille")
        texte(int(425*coef_largeur), int(400*coef_hauteur),"Taille", "white", "center", taille=int(32*coef_hauteur), tag="Variante Taille" )
    else:
        rectangle(int(275*coef_largeur), int(350*coef_hauteur),int( 575*coef_largeur), int(450*coef_hauteur), "white", "red", 5, tag="Variante Taille")
        texte(int(425*coef_largeur), int(400*coef_hauteur), "Taille", "white", "center", taille=int(32*coef_hauteur), tag="Variante Taille" )
    if Dynamique:
        rectangle(int(625*coef_largeur), int(350*coef_hauteur), int(925*coef_largeur), int(450*coef_hauteur), "white", "green", 5, tag="Variante Dynamique")
        texte(int(775*coef_largeur), int(400*coef_hauteur), "Dynamique", "white", "center", taille=int(32*coef_hauteur), tag="Variante Dynamique" )
    else:
        rectangle(int(625*coef_largeur), int(350*coef_hauteur), int(925*coef_largeur), int(450*coef_hauteur), "white", "red", 5, tag="Variante Dynamique")
        texte(int(775*coef_largeur), int(400*coef_hauteur), "Dynamique", "white", "center", taille=int(32*coef_hauteur), tag="Variante Dynamique" )
    if Terminaison:
        rectangle(int(275*coef_largeur), int(500*coef_hauteur),int( 575*coef_largeur), int(600*coef_hauteur), "white", "green", 5, tag="Variante Terminaison")
        texte(int(425*coef_largeur), int(550*coef_hauteur),"Terminaison", "white", "center", taille=int(32*coef_hauteur), tag="Variante Terminaison" )
    else:
        rectangle(int(275*coef_largeur), int(500*coef_hauteur), int(575*coef_largeur), int(600*coef_hauteur), "white", "red", 5, tag="Variante Terminaison")
        texte(int(425*coef_largeur), int(550*coef_hauteur), "Terminaison", "white", "center", taille=int(32*coef_hauteur), tag="Variante Terminaison" )
    if Obstacle:
        rectangle(int(625*coef_largeur), int(500*coef_hauteur),int( 925*coef_largeur), int(600*coef_hauteur), "white", "green", 5, tag="Variante Obstacle")
        texte(int(775*coef_largeur), int(550*coef_hauteur), "Obstacle", "white", "center", taille=int(32*coef_hauteur), tag="Variante Obstacle" )
    else:
        rectangle(int(625*coef_largeur), int(500*coef_hauteur),int( 925*coef_largeur), int(600*coef_hauteur), "white", "red", 5, tag="Variante Obstacle")
        texte(int(775*coef_largeur), int(550*coef_hauteur), "Obstacle", "white", "center", taille=int(32*coef_hauteur), tag="Variante Obstacle" )

    rectangle(int(1130*coef_largeur), int(680*coef_hauteur),int( 1230*coef_largeur), int(715*coef_hauteur), "black","red", 1, "Variante")
    texte(int(1143*coef_largeur), int(685*coef_hauteur), "Retour", "white", "nw", taille=int(16*coef_hauteur), tag="Variante")
    mise_a_jour()

######################## Fonctions d'ajout et de choix des variants/option #######################################################

def fond_sablier(temps, t1):
    """ 
    Affiche un temps qui s'écoule où 'temps' est le temps maximum que doit prendre un jouer pour jouer
    et 't1' le temps qui augmente tant que le joueur ne joue pas.
    """
    efface("Sablier")
    texte(int(640*coef_largeur), int(80*coef_hauteur), str(round(temps-t1, 1)), "white", "center", taille = int(20*coef_hauteur), tag = "Sablier Jeu")
    mise_a_jour()

def fond_score(score):
    texte(int(250*coef_largeur), int(50*coef_hauteur), "Score du Joueur", "black", "w", taille = int(20*coef_hauteur), tag = "Scores Jeu")
    cercle(int(475*coef_largeur), int(50*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[0], tag="Scores Jeu")
    texte(int(495*coef_largeur), int(50*coef_hauteur), " : " + str(score[0]), "black", "w", taille = int(20*coef_hauteur), tag = "Scores Jeu")
    texte(int(675*coef_largeur), int(50*coef_hauteur), "Score du Joueur", "black", "w", taille = int(20*coef_hauteur), tag = "Scores Jeu")
    cercle(int(900*coef_largeur), int(50*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[1], tag="Scores Jeu")
    texte(int(920*coef_largeur), int(50*coef_hauteur), " : " + str(score[1]), "black", "w", taille = int(20*coef_hauteur), tag = "Scores Jeu")
    mise_a_jour()

def fleches(direction, x, y):
    rectangle(x, y, x+int(25*coef_largeur), y+int(30*coef_hauteur), "black", "red", tag="Taille Jeu")
    if direction == "gauche":
        polygone([x+int(18*coef_largeur), y+int(2*coef_hauteur),x+int(5*coef_largeur), y+int(15*coef_hauteur), x+int( 18*coef_largeur), y+int(28*coef_hauteur)], "darkred", "darkred", tag="Taille Jeu")
    else:
        polygone([x+int(7*coef_largeur), y+int(2*coef_hauteur),x+int(20*coef_largeur), y+int(15*coef_hauteur), x+int(7*coef_largeur), y+int(28*coef_hauteur)], "darkred", "darkred", tag="Taille Jeu")

def fond_taille():
    texte(int(50*coef_largeur), int(695*coef_hauteur), "Montant à poser:", "black", "w", taille=int(20*coef_hauteur), tag="Taille Jeu")
    # Centaines
    fleches("gauche", int(260*coef_largeur), int(680*coef_hauteur))
    fleches("droite", int(320*coef_largeur), int(680*coef_hauteur))
    rectangle(int(290*coef_largeur), int(680*coef_hauteur), int(315*coef_largeur), int(710*coef_hauteur), "darkcyan", "floralwhite", tag="Taille Jeu")
    texte(int(303*coef_largeur), int(695*coef_hauteur), "0", "black", "center", taille=int(24*coef_hauteur), tag="centaine Jeu")
    # Dizanes
    fleches("gauche", int(360*coef_largeur), int(680*coef_hauteur))
    fleches("droite", int(420*coef_largeur), int(680*coef_hauteur))
    rectangle(int(390*coef_largeur), int(680*coef_hauteur), int( 415*coef_largeur), int(710*coef_hauteur), "darkcyan", "floralwhite", tag="Taille Jeu")
    texte(int(403*coef_largeur), int(695*coef_hauteur), "0", "black", "center", taille=int(24*coef_hauteur), tag="dizaine Jeu")
    # Unites
    fleches("gauche", int(460*coef_largeur), int(680*coef_hauteur))
    fleches("droite", int(520*coef_largeur), int(680*coef_hauteur))
    rectangle(int(490*coef_largeur), int(680*coef_hauteur), int( 515*coef_largeur), int(710*coef_hauteur), "darkcyan", "floralwhite", tag="Taille Jeu")
    texte(int(503*coef_largeur), int(695*coef_hauteur), "0", "black", "center", taille=int(24*coef_hauteur), tag="unite Jeu")
    mise_a_jour()

def epargne_joueurs(epargne_1, epargne_2):
    efface("epargne")
    texte(int(600*coef_largeur), int(695*coef_hauteur), "Montant", "black", "w", taille=int(20*coef_hauteur), tag="epargne Jeu")
    cercle(int(725*coef_largeur), int(695*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[0], tag="epargne Jeu")
    texte(int(745*coef_largeur), int(695*coef_hauteur), " :" + str(epargne_1), "black", "w", taille=int(20*coef_hauteur), tag="epargne Jeu")
    texte(int(850*coef_largeur), int(695*coef_hauteur), "Montant", "black", "w", taille=int(20*coef_hauteur), tag="epargne Jeu")
    cercle(int(975*coef_largeur), int(695*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[1], tag="epargne Jeu")
    texte(int(995*coef_largeur), int(695*coef_hauteur), " : " + str(epargne_2), "black", "w", taille=int(20*coef_hauteur), tag="epargne Jeu")
    mise_a_jour()

def variante_score(score, t_sablier):
    fond_score(score)
    temps = time() + 2
    while time() < temps:
        ev = donne_evenement()
        mise_a_jour()
        type_ev = type_evenement(ev)
        if type_ev == 'ClicGauche':
            efface("Scores")
            mise_a_jour()
            x, y = clic_x(ev), clic_y(ev)
            if t_sablier != None:
                return x, y, time()
            return x, y
    efface("Scores")
    mise_a_jour()

    if t_sablier != None:
        return None, None, t_sablier + 2
    return None, None

def variante_taille(x, y, centaine, dizaine, unite):
    efface("centaine")
    efface("dizaine")
    efface("unite")
    if  int(680*coef_hauteur) <= y <=  int(710*coef_hauteur):
        if int(260*coef_largeur) <= x <= int(285*coef_largeur):
            centaine = (centaine-1) % 10
        elif int(320*coef_largeur) <= x <= int(345*coef_largeur):
            centaine = (centaine+1) % 10
        elif int(360*coef_largeur) <= x <= int(385*coef_largeur):
            dizaine = (dizaine-1) % 10
        elif int(420*coef_largeur) <= x <= int(445*coef_largeur):
            dizaine = (dizaine+1) % 10
        elif int(460*coef_largeur) <= x <= int(485*coef_largeur):
            unite = (unite-1) % 10
        elif int(520*coef_largeur) <= x <= int(545*coef_largeur):
            unite = (unite+1) % 10
    texte(int(303*coef_largeur), int(695*coef_hauteur), str(centaine), "black", "center", taille=int(24*coef_hauteur), tag="centaine Jeu")
    texte(int(403*coef_largeur), int(695*coef_hauteur), str(dizaine), "black", "center", taille=int(24*coef_hauteur), tag="dizaine Jeu")
    texte(int(503*coef_largeur), int(695*coef_hauteur), str(unite), "black", "center", taille=int(24*coef_hauteur), tag="unite Jeu")
    mise_a_jour()
    return centaine, dizaine, unite

def variante_terminaison(numero_tour):
    nb_max_tour = numero_tour + 5
    return nb_max_tour

def creer_obstacles():
    """
    Créer une liste correspondant aux informations des différents obstacles représenté par des boules.
    """
    liste_obstacle = []
    for i in range(10):
        r = randint(25, 50)
        x, y = randint(50+r, 1230-r), randint(100+r, 670-r)
        tag = cercle(x, y, r, "gray", "gray", tag="Jeu")
        liste_obstacle.append((x, y, r, tag))
    return liste_obstacle

def detecter_intersection(x, y, rayon, liste_obstacle):
    """
    Permet de détecter si un cercle est en intersection avec un obstacle
    les parametres 'x', 'y' et 'rayon' correspondent aux informations du clique et du rayon du futur cercle
    le paramètre liste_obstacle nous permet de tester les intersections avec les obstacles grâces aux informations les concernant
    """
    for i in range(len(liste_obstacle)):
        distance = sqrt((x-liste_obstacle[i][0])**2 + (y-liste_obstacle[i][1])**2)
        if distance < liste_obstacle[i][2] + rayon:
            return True
    return None

def variante_dynamique(liste_cercle_un, liste_cercle_deux, couleur, Obstacle, liste_obstacle):
    """
    Permet d'augmenter le rayon de toute les boules présente sur le terrain d'un certain nombre de pixel
    les paramètres liste_cercle_un et liste_cercle_deux représente les listes des cercles des deux joueurs
    la couleur permet de créer les cercles de couleur
    obstacle et liste_bostacle sont nécessaire pour tester si les cercles sont en intersection avec les obstacles
    """
    for i in range(5):
        for i in range(len(liste_cercle_un)):
            intersection = 0
            x, y, r = liste_cercle_un[i][0], liste_cercle_un[i][1], liste_cercle_un[i][2]+1
            if Obstacle:
                if detecter_intersection(x, y, r, liste_obstacle) == True:
                    intersection += 1
            for element in liste_cercle_deux:
                distance = sqrt((x - element[0])**2 + (y-element[1])**2)
                if distance < element[2] + r:
                    intersection += 1

            liste = calcul_extremite_cercle(liste_cercle_un[i], r)
            if liste[0]<50 or liste[1]>1230 or liste[2]<100 or liste[3]>670:
                intersection += 1
                
            if intersection == 0:
                efface(liste_cercle_un[i][3])
                id_cercle = cercle(x, y, r, "black", couleur, tag="Jeu")
                liste_cercle_un[i] = [x, y, r, id_cercle]
    return liste_cercle_un

######################## Fonctions de sauvegarde ##################################################################################

def detection_sauvegarde():
    while True:
        x, y, z = attente_clic()
        if int(490*coef_largeur) <= x <= int(790*coef_largeur) :
            if int(200*coef_hauteur) <= y <= int(300*coef_hauteur):
                Sauvegarde = 1
                break
            elif int(350*coef_hauteur) <= y <= int(450*coef_hauteur):
                Sauvegarde = 2
                break
            elif int(500*coef_hauteur) <= y <= int(600*coef_hauteur):
                Sauvegarde = 3
                break
    return Sauvegarde

def creation_sauvegarde(num, nb_max_tour):
    ligne = []
    liste_valeurs = [[], [], 0, 1, nb_max_tour, epargne_1, epargne_2]
    fichier = open(os.sep.join(["Fichiers", "Sauvegarde"]) + str(num) + ".txt", "w")
    for i in range(len(liste_variables)):
        ligne.append(liste_variables[i] + " : " + str(liste_valeurs[i]) + "\n")
    fichier.writelines(ligne)
    fichier.close()

def chargement(num):
    fichier = open(os.sep.join(["Fichiers", "Sauvegarde"]) + str(num) + ".txt", "r")
    sauvegardes = []
    for lignes in fichier:
        if lignes[len(lignes)-1] == "\n":
            sauvegardes.append(lignes[:-1])
        else:
            sauvegardes.append(lignes)
    fichier.close()
    for i in range(len(sauvegardes)):
        sauvegardes[i] = sauvegardes[i].split(":")
    variables = []
    for i in range(len(sauvegardes)):
            variables.append(json.loads(sauvegardes[i][-1].strip()))
    return variables

def maj_sauvegarde(num_sauv, liste_valeurs):
    fichier = open(os.sep.join(["Fichiers", "Sauvegarde"]) + str(num_sauv) + ".txt", "w")
    for i in range(len(liste_variables)):
        fichier.write(liste_variables[i] + " : " + str(liste_valeurs[i]) + "\n")
    fichier.close()

######################## Fonctions de detection ##################################################################################

def detection_variante(Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter, Sauvegarde):
    while True:
        x, y, z = attente_clic()
        if int(200*coef_largeur) <= x <= int(600*coef_largeur) :
            if int(300*coef_hauteur) <= y <= int(400*coef_hauteur):
                efface("Menu")
                fond_jeu()
                break
            elif int(450*coef_hauteur) <= y <= int(550*coef_hauteur):
                efface("Menu")
                variantes(Sablier, Scores, Taille, Dynamique, Terminaison, Obstacle)
                while True:
                    x, y, z = attente_clic()
                    if int(275*coef_largeur) <= x <= int(575*coef_largeur) and int(200*coef_hauteur) <= y <= int(300*coef_hauteur):
                        if not Sablier:
                            Sablier = True
                        else:
                            Sablier = False
                    elif int(625*coef_largeur) <= x <= int(925*coef_largeur) and int(200*coef_hauteur) <= y <= int(300*coef_hauteur):
                        if not Scores:
                            Scores = True
                        else:
                            Scores = False
                    elif int(275*coef_largeur) <= x <= int(575*coef_largeur) and int(350*coef_hauteur) <= y <= int(450*coef_hauteur):
                        if not Taille:
                            Taille = True
                        else:
                            Taille = False
                    elif int(625*coef_largeur) <= x <= int(925*coef_largeur) and int(350*coef_hauteur) <= y <= int(450*coef_hauteur):
                        if not Dynamique:
                            Dynamique = True
                        else:
                            Dynamique = False
                    elif int(275*coef_largeur) <= x <= int(575*coef_largeur) and int(500*coef_hauteur) <= y <= int(600*coef_hauteur):
                        if not Terminaison:
                            Terminaison = True
                        else:
                            Terminaison = False
                    elif int(625*coef_largeur) <= x <= int(925*coef_largeur) and int(500*coef_hauteur) <= y <= int(600*coef_hauteur):
                        if not Obstacle:
                            Obstacle = True
                        else:
                            Obstacle = False
                    elif int(1130*coef_largeur) <=x<= int(1230*coef_largeur) and int(680*coef_hauteur) <=y<=int(715*coef_hauteur):
                        efface("Variante")
                        fond_menu()
                        break
                    variantes(Sablier, Scores, Taille, Dynamique, Terminaison, Obstacle)
        elif int(650*coef_largeur) <= x <= int(1050*coef_largeur):
            if int(450*coef_hauteur) <= y <= int(550*coef_hauteur):
                Quitter = True
                break
            elif int(300*coef_hauteur) <= y <= int(400*coef_hauteur):
                efface("Menu")
                fond_sauvegarde()
                Sauvegarde = detection_sauvegarde()
                efface("Sauvegarde")
                fond_menu()
    return Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter, Sauvegarde

def clic_hors_bordure(x, y):
    """ 
    Redemande au joueur de cliquer dans la zone lorsque les coordonnées 'x' et 'y' ne sont pas respectées.
    """
    if int(1130*coef_largeur) <= x <= int(1230*coef_largeur) and int(680*coef_hauteur) <= y <= int(715*coef_hauteur):
        return x, y
    while x < int(50*coef_largeur) or x > int(1230*coef_largeur) or y < int(100*coef_hauteur) or y > int(670*coef_hauteur):
        x, y, m = attente_clic()
        if int(1130*coef_largeur) <= x <= int(1230*coef_largeur) and int(680*coef_hauteur) <= y <= int(715*coef_hauteur):
            break
    return x, y

def clic_hors_retour(x,y):
    while x > int(1230*coef_largeur) or x < int(1130*coef_largeur) or y < int(680*coef_hauteur) or y >int(715*coef_hauteur):
        x, y, m = attente_clic()
    return x, y

def detection_tour(tour, numero_tour, nb_max_tour):
    """ 
    Affiche les textes indiquant à qui est le tour et le nombre de tour que les joueurs ont effectués où :
    tour : indique à quel joueur c'est au tour de jouer (paramètre : int) (valeur : '0' ou '1' pour respectivement Joueur 1 ou Joueur 2)
    listeJoueur : indique la liste des joueurs qui jouent (paramètre : str)
    numero_tour : indique le nombre de tours joués (paramètre : int)
    nb_max_tour : indique le nombre maximum de tours (paramètre : int)
    """
    efface("tour")
    cercle(int(160*coef_largeur), int(50*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[tour], tag="tour Jeu")
    texte(int(50*coef_largeur), int(50*coef_hauteur), "Tour :", "lightcyan", "w", taille=int(24*coef_hauteur), tag="tour Jeu")
    texte(int(1230*coef_largeur), int(50*coef_hauteur), "Tour n° "+ str(numero_tour) + "/"+str(nb_max_tour), "lightcyan", "e", taille=int(24*coef_hauteur), tag="tour Jeu")

def detection_cercle_inscrit(alterner_liste_joueur):
    """
    Permet de detecter si un cercle est caché derrière un autre cercle qui à été posé par dessus, si cela est le cas, la fonction supprime le cercle caché.
    alterner_liste_joueur : c'est une variable temporaire qui permet d'alterner entre les deux listes des deux différents joueurs
    """
    liste = []
    for i in range(len(alterner_liste_joueur)-1):
        dernier_cercle = alterner_liste_joueur[-1]
        cercle = alterner_liste_joueur[i]
        distance = sqrt((cercle[0]-dernier_cercle[0])**2 + (cercle[1]-dernier_cercle[1])**2)
        if distance + cercle[2] <= dernier_cercle[2]:
            efface(cercle[3])
            liste.append(cercle)
    for i in range(len(liste)):
        alterner_liste_joueur.remove(liste[i])

######################## Fonctions agissant directement sur le terrain de jeu ####################################################

def calcul_extremite_cercle(cercle, r):
    """
    Cette fonction permet de créer une liste avec les cordonnée des quatres extrémité d'un cercle
    """
    liste = [cercle[0]-r,cercle[0]+r,cercle[1]-r,cercle[1]+r]
    return liste

def calcul_score(liste_cercle):
    ensemble = set()
    for element in liste_cercle:
        for x in range(element[0]-element[2], element[0]+element[2]+1):
            for y in range(element[1]-element[2], element[1]+element[2]+1):
                distance = sqrt((x-element[0])**2 + (y-element[1])**2)
                if distance <= element[2]:
                    ensemble.add((x, y))
    if ensemble == {}:
        return None
    return ensemble

def scinder(x, y, liste_cercle_2, liste_cercle_1, element, distance, tour):
    """
    Permet la division des cercles lorsque un joueur clique sur le cercle adverse.
    x, y (float/int) : cordonnées x et y du clic du joueur dans le terrain de jeu
    liste_cercle_2 (list) : liste contenant les informations sur les différents cercle du joueur vert sur le terrain
    liste_cercle_1 (list) : liste contenant les informations sur les différents cercle du joueur violet sur le terrain
    element (list) : indique sur quel cercle la fonction est en train d'agir (l'element est une liste constitué d'information sur le cercle)
    distance (float/int) : indique le distance entre le clic du joueur et le centre du cercle adverse déjà présent sur le terrain
    tour (int) : indique le tour du joueur si le clic se fait par le joueur a sur un cercle du joueur b ou vice versa
    couleurJoueur (list) : indique la couleur des deux cercles qui vont se créer lors du scindement
    """
    tour = (tour+1) % 2
    rayon1 = int(element[2]-sqrt(distance))
    rayon2 = int(element[2]-rayon1)
    
    if x - element[0] == 0:
        m2 = x
    else:
        m2 = (y-element[1])/(x-element[0])
    m1 = 0
    calcul = abs((m2-m1)/(1+m1*m2))
    gamma = atan(calcul) * (180/pi)
    alpha = (90-gamma) * (pi/180)
    x2 = sin(alpha)*rayon1
    y2 = cos(alpha)*rayon1
    if element[0]-x < 0:
        x2 = int(element[0]-x2)
    else:
        x2 = int(element[0]+x2)
    if element[1]-y < 0:
        y2 = int(element[1]-y2)
    else:
        y2 = int(element[1]+y2)

    tag1 = cercle(x, y, rayon1, "black", couleurJoueur[tour], 1, tag="Jeu")
    tag2 = cercle(x2, y2, rayon2, "black", couleurJoueur[tour], 1, tag="Jeu")
    if tour == 0:
        liste_cercle_2.append([x, y, rayon1, tag1])
        liste_cercle_2.append([x2, y2, rayon2, tag2])
        liste_cercle_2.pop(liste_cercle_2.index(element))
    else:
        liste_cercle_1.append([x2, y2, rayon2, tag2])  
        liste_cercle_1.append([x, y, rayon1, tag1])
        liste_cercle_1.pop(liste_cercle_1.index(element))
    efface(element[3])

def cerkle(x, y, tour, liste_cercle_2, liste_cercle_1, rayon):
    """
    Cette fonction permet d'afficher les cercles et les intègre dans une liste pour garder les différentes informations tel que :
    x, y : cordonnées x et y du centre du cercle
    rayon : indique le rayon du cercle prochainement généré
    """
    id_cercle = cercle(x, y, rayon, "black", couleurJoueur[tour], 1, tag="Jeu")
    if tour == 0:
        liste_cercle_2.append([x, y, rayon, id_cercle])
    else:
        liste_cercle_1.append([x, y, rayon, id_cercle])

def main():
    cree_fenetre(largeur_fenetre, hauteur_fenetre)
    rectangle(-1,-1, largeur_fenetre, hauteur_fenetre,"darkcyan","darkcyan")
    Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter = [False]*7
    fond_sauvegarde()
    Sauvegarde = detection_sauvegarde()
    efface("Sauvegarde")
    if not os.path.exists(os.sep.join(["Fichiers", "Sauvegarde" + str(Sauvegarde) + ".txt"])):
        nb_max_tour = int(config[5][-1].strip())
        creation_sauvegarde(Sauvegarde, nb_max_tour)
    while True:
        Retour = False
        fond_menu()
        Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter, Sauvegarde = detection_variante(Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter, Sauvegarde)
        if not os.path.exists(os.sep.join(["Fichiers", "Sauvegarde" + str(Sauvegarde) + ".txt"])):
            nb_max_tour = int(config[5][-1].strip())
            creation_sauvegarde(Sauvegarde, nb_max_tour)
        if not Quitter:
            # Variables
            liste_cercle_1_temp, liste_cercle_2_temp, tour, numero_tour, nb_max_tour, epargne_1, epargne_2 = chargement(Sauvegarde)
            liste_obstacle = []
            rayon = int(config[2][-1])
            score=[0, 0]
            alterner_liste_joueur, b = liste_cercle_1, liste_cercle_2
            detection_terminaison = 0
            detection_obstacle = 0
            # Variante taille de boule
            if Taille:
                centaine = 0
                dizaine = 0
                unite = 0 
                fond_taille()
                epargne_joueurs(epargne_1, epargne_2)
            while not Retour:
                if numero_tour < nb_max_tour+1:
                    x = None
                    detection_tour(tour, numero_tour, nb_max_tour)
                    if Sablier:
                        t = 0
                        temps = time() + int(config[7][-1])
                        while time() - t < temps:
                            ev = donne_evenement()
                            mise_a_jour()
                            type_ev = type_evenement(ev)
                            fond_sablier(temps, time() - t)
                            if type_ev == "ClicGauche":
                                x, y = clic_x(ev), clic_y(ev)
                                if Taille:
                                    centaine, dizaine, unite = variante_taille(x, y, centaine, dizaine, unite)
                                if int(1130*coef_largeur)<=x<=int(1230*coef_largeur) and int(680*coef_hauteur)<=y<=int(715*coef_hauteur):
                                    break
                                elif x<int(50*coef_largeur) or x>int(1230*coef_largeur) or y<int(100*coef_hauteur) or y>int(670*coef_hauteur):
                                    continue
                                break
                            elif type_ev == "Touche":
                                if Scores and touche(ev) == config[9][-1].strip():
                                    x, y, t = variante_score(score, t)
                                    if x != None:
                                        break
                                    continue
                                if Terminaison and detection_terminaison == 0 and touche(ev) == config[8][-1].strip():
                                    nb_max_tour = variante_terminaison(numero_tour)
                                    detection_terminaison += 1
                                    if x != None:
                                        break
                                    continue
                            elif Obstacle and detection_obstacle == 0:
                                liste_obstacle = creer_obstacles()
                                detection_obstacle = 1
                            
                        if x == None:
                            if tour == 1:
                                numero_tour += 1
                            tour = (tour+1) % 2
                            alterner_liste_joueur, b = b, alterner_liste_joueur
                            mise_a_jour()
                            continue

                    elif Scores:
                        ev = donne_evenement()
                        mise_a_jour()
                        type_ev = type_evenement(ev)
                        if type_ev == 'ClicGauche':
                            x, y = clic_x(ev), clic_y(ev)
                        elif type_ev == 'Touche':
                            if touche(ev) == config[9][-1].strip():
                                x, y = variante_score(score, None) 
                                if x == None:
                                    continue
                            elif Terminaison and detection_terminaison == 0 and touche(ev) == config[8][-1].strip():
                                nb_max_tour = variante_terminaison(numero_tour)
                                detection_terminaison += 1
                                if x != None:
                                    break
                                continue
                            else:
                                continue
                        elif Obstacle and detection_obstacle == 0:
                            liste_obstacle = creer_obstacles()
                            detection_obstacle = 1
                        else:
                            continue

                    elif Obstacle and detection_obstacle == 0:
                        liste_obstacle = creer_obstacles()
                        detection_obstacle = 1

                    elif Terminaison and detection_terminaison == 0:
                        ev = donne_evenement()
                        mise_a_jour()
                        type_ev = type_evenement(ev)
                        if type_ev == 'ClicGauche':
                            x, y = clic_x(ev), clic_y(ev)
                        elif type_ev == 'Touche':
                            if touche(ev) == config[8][-1].strip():
                                nb_max_tour = variante_terminaison(numero_tour)
                                detection_terminaison += 1
                            else:
                                continue        
                        else:
                            continue
                    if x == None:
                        x, y, w = attente_clic()
                    
                    if Taille:
                        centaine, dizaine, unite = variante_taille(x, y, centaine, dizaine, unite)
                        depense = centaine*100 + dizaine*10 + unite
                        if int(1130*coef_largeur)<=x<=int(1230*coef_largeur) and int(680*coef_hauteur)<=y<=int(715*coef_hauteur):
                            break
                        elif x < int(50*coef_largeur) or x > int(1230*coef_largeur) or y < int(100*coef_hauteur) or y > int(670*coef_hauteur):
                            continue
                        elif int(50*coef_largeur) <= x <= int(1230*coef_hauteur) and int(100*coef_hauteur) <= y <= int(670*coef_hauteur):
                            if tour == 0:
                                if epargne_1 - depense < 0:
                                    continue
                                else:
                                    epargne_1 -= depense
                                    rayon = depense
                            else:
                                if epargne_2 - depense < 0:
                                    continue
                                else:
                                    epargne_2 -= depense
                                    rayon = depense
                            epargne_joueurs(epargne_1, epargne_2)

                    x, y = clic_hors_bordure(x, y)
                    if int(1130*coef_largeur) <= x <= int(1230*coef_largeur) and int(680*coef_hauteur) <= y <= int(715*coef_hauteur):
                        Retour = True
                        break

                    if int(50*coef_largeur) <= x < int(50*coef_largeur)+rayon:
                        x = int(50*coef_largeur)+rayon
                    elif int(1230*coef_largeur)-rayon < x <= int(1230*coef_largeur):
                        x = int(1230*coef_largeur)-rayon
                        
                    if int(100*coef_hauteur) <= y < int(100*coef_hauteur)+rayon:
                        y = int(100*coef_hauteur)+rayon
                    elif int(670*coef_hauteur)-rayon <y <= int(670*coef_hauteur):
                        y = int(670*coef_hauteur)-rayon

                    if tour == 1:
                        numero_tour += 1
                            
                    intersection_cercle = 0

                    for i in range(len(alterner_liste_joueur)-1, -1, -1):
                        element = alterner_liste_joueur[i]
                        distance = (x-alterner_liste_joueur[i][0])**2 + (y-alterner_liste_joueur[i][1])**2
                        if sqrt(distance) < alterner_liste_joueur[i][2] + rayon and sqrt(distance) > alterner_liste_joueur[i][2]:
                            intersection_cercle += 1
                        elif sqrt(distance) < alterner_liste_joueur[i][2]:
                            scinder(x, y, alterner_liste_joueur, liste_cercle_1, element, distance, tour)
                            intersection_cercle += 1
                    print(liste_cercle_1)
                    print(liste_cercle_2)
                    
                    if Obstacle and detecter_intersection(x, y, rayon, liste_obstacle) == True:
                        intersection_cercle += 1
                            
                    alterner_liste_joueur, b = b, alterner_liste_joueur

                    if intersection_cercle == 0 and rayon != 0:
                        cerkle(x, y, tour, liste_cercle_2, liste_cercle_1, rayon)

                        detection_cercle_inscrit(alterner_liste_joueur)

                    score[0] = len(calcul_score(liste_cercle_2))
                    score[1] = len(calcul_score(liste_cercle_1))
                    if numero_tour == nb_max_tour+1 and tour == 1:
                        if score[0] > score[1]:
                            texte(int(500*coef_largeur), int(50*coef_hauteur),"Le Joueur", "white", "w",  taille=int(24*coef_hauteur), tag="Jeu")
                            cercle(int(670*coef_largeur), int(50*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[0], tag="Scores Jeu")
                            texte(int(690*coef_largeur), int(50*coef_hauteur)," gagne", "white", "w",  taille=int(24*coef_hauteur), tag="Jeu")

                        elif score[1] > score[0]:
                            texte(int(500*coef_largeur), int(50*coef_hauteur),"Le Joueur", "white", "w",  taille=int(24*coef_hauteur), tag="Jeu")
                            cercle(int(670*coef_largeur), int(50*coef_hauteur), int(20*coef_hauteur), "black", couleurJoueur[1], tag="Scores Jeu")
                            texte(int(690*coef_largeur), int(50*coef_hauteur)," gagne", "white", "w",  taille=int(24*coef_hauteur), tag="Jeu")
                        else:
                            texte(int(640*coef_largeur), int(50*coef_hauteur), "Egalité", "white", "center", taille=int(24*coef_hauteur), tag="Jeu")
                       
                        x, y, z = attente_clic()
                        x, y = clic_hors_retour(x,y)
                        Retour = True
                    
                    if Dynamique:
                        variante_dynamique(alterner_liste_joueur, b, couleurJoueur[tour], Obstacle, liste_obstacle)
                        variante_dynamique(b, alterner_liste_joueur, couleurJoueur[(tour+1)%2], Obstacle, liste_obstacle)
                                
                    tour = (tour+1) % 2 
                    
                    mise_a_jour()
            
            efface("Jeu")
            mise_a_jour()
            if tour == 0:
                liste_cercle_1, liste_cercle_2 == alterner_liste_joueur, b
            else:
                liste_cercle_1, liste_cercle_2 == b, alterner_liste_joueur
            liste_valeurs = [liste_cercle_1, liste_cercle_2, tour, numero_tour, nb_max_tour, epargne_1, epargne_2]
            maj_sauvegarde(Sauvegarde, liste_valeurs)
            if numero_tour == nb_max_tour+1 and tour == 0:
                creation_sauvegarde(Sauvegarde, nb_max_tour)
        else:
            break
            
    ferme_fenetre()

if __name__ == '__main__':
    main()
