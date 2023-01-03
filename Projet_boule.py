from upemtk import *
from random import *
from time import *
from math import *

largeur_fenetre = 1920
hauteur_fenetre = 500
coef_largeur = largeur_fenetre/1280
coef_hauteur = hauteur_fenetre/720

######################## Fonction d'aspect graphique des différents affichages ###################################################

def fond_menu(): # Affiche le menu du jeu
    rectangle(int(2*coef_largeur), int(2*coef_hauteur), int(1277*coef_largeur), int(150*coef_hauteur), "white", epaisseur=5, tag="Menu")
    texte(int(640*coef_largeur), int(75*coef_hauteur), "Bataille des boules", "white", "center", taille=int(50*coef_hauteur), tag="Menu")

    rectangle(int(490*coef_largeur), int(200*coef_hauteur), int( 790*coef_largeur), int(300*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(640*coef_largeur), int(250*coef_hauteur), "Jouer", "white", "center", taille=int(40*coef_hauteur), tag="Menu")

    rectangle(int(490*coef_largeur), int(350*coef_hauteur), int(790*coef_largeur), int(450*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(640*coef_largeur), int(400*coef_hauteur), "Variantes", "white", "center", taille=int(40*coef_hauteur), tag="Menu")

    rectangle(int(490*coef_largeur), int(500*coef_hauteur),int( 790*coef_largeur), int(600*coef_hauteur), "white", "#009382", 5, tag="Menu")
    texte(int(640*coef_largeur),int(550*coef_hauteur),"Quitter", "white", "center", taille=int(40*coef_hauteur), tag="Menu")
    mise_a_jour()

def fond_jeu(): # Affiche les éléments du terrains de jeu
    rectangle(int(50*coef_largeur), int(100*coef_hauteur), int(1230*coef_largeur), int(670*coef_hauteur), "floralwhite","floralwhite")

    rectangle(int(1130*coef_largeur), int(680*coef_hauteur), int(1230*coef_largeur), int(715*coef_hauteur), "black","red", 1, "Quitter")
    texte(int(1180*coef_largeur), int(698*coef_hauteur), "Quitter", "white", "c", taille=int(16*coef_hauteur))

    texte(0,0,"",tag="tour")
    texte(0,0,"",tag="tour2")
    mise_a_jour()

def variantes(Sablier, Scores, Taille, Dynamique, Terminaison, Obstacle): # Affiche le menu des variantes pour choisir une ou plusieurs variantes (pour l'instant seul le sablier est disponible)
    efface("Variante")
    rectangle(int(2*coef_largeur),int(2*coef_hauteur), int(1277*coef_largeur), int(150*coef_hauteur), "white", epaisseur=5, tag="Variante")
    texte(int(640*coef_largeur), int(75*coef_hauteur), "Variantes", "white", "center", taille=int(50*coef_hauteur), tag="Variante")
    if Sablier:
        rectangle(int(275*coef_largeur), int(200*coef_hauteur), int( 575*coef_largeur), int(300*coef_hauteur), "white", "green", 5, tag="Sablier")
        texte(int(425*coef_largeur), int(250*coef_hauteur), "Sablier", "white", "center", taille=int(32*coef_hauteur), tag="Sablier")
    else:
        rectangle(int(275*coef_largeur), int(200*coef_hauteur), int( 575*coef_largeur), int(300*coef_hauteur), "white", "red", 5, tag="Sablier")
        texte(int(425*coef_largeur), int(250*coef_hauteur), "Sablier", "white", "center", taille=int(32*coef_hauteur), tag="Sablier")
    if Scores:
        rectangle(int(625*coef_largeur), int(200*coef_hauteur), int( 925*coef_largeur), int(300*coef_hauteur), "white", "green", 5, tag="Scores")
        texte(int(775*coef_largeur), int(250*coef_hauteur), "Scores", "white", "center", taille=int(32*coef_hauteur), tag="Scores" )
    else:
        rectangle(int(625*coef_largeur), int(200*coef_hauteur),int( 925*coef_largeur), int(300*coef_hauteur), "white", "red", 5, tag="Scores")
        texte(int(775*coef_largeur), int(250*coef_hauteur),"Scores", "white", "center", taille=int(32*coef_hauteur), tag="Scores" )
    if Taille:
        rectangle(int(275*coef_largeur), int(350*coef_hauteur),int( 575*coef_largeur), int(450*coef_hauteur), "white", "green", 5, tag="Taille")
        texte(int(425*coef_largeur), int(400*coef_hauteur),"Taille", "white", "center", taille=int(32*coef_hauteur), tag="Taille" )
    else:
        rectangle(int(275*coef_largeur), int(350*coef_hauteur),int( 575*coef_largeur), int(450*coef_hauteur), "white", "red", 5, tag="Taille")
        texte(int(425*coef_largeur), int(400*coef_hauteur), "Taille", "white", "center", taille=int(32*coef_hauteur), tag="Taille" )
    if Dynamique:
        rectangle(int(625*coef_largeur), int(350*coef_hauteur), int(925*coef_largeur), int(450*coef_hauteur), "white", "green", 5, tag="Dynamique")
        texte(int(775*coef_largeur), int(400*coef_hauteur), "Dynamique", "white", "center", taille=int(32*coef_hauteur), tag="Dynamique" )
    else:
        rectangle(int(625*coef_largeur), int(350*coef_hauteur), int(925*coef_largeur), int(450*coef_hauteur), "white", "red", 5, tag="Dynamique")
        texte(int(775*coef_largeur), int(400*coef_hauteur), "Dynamique", "white", "center", taille=int(32*coef_hauteur), tag="Dynamique" )
    if Terminaison:
        rectangle(int(275*coef_largeur), int(500*coef_hauteur),int( 575*coef_largeur), int(600*coef_hauteur), "white", "green", 5, tag="Terminaison")
        texte(int(425*coef_largeur), int(550*coef_hauteur),"Terminaison", "white", "center", taille=int(32*coef_hauteur), tag="Terminaison" )
    else:
        rectangle(int(275*coef_largeur), int(500*coef_hauteur), int(575*coef_largeur), int(600*coef_hauteur), "white", "red", 5, tag="Terminaison")
        texte(int(425*coef_largeur), int(550*coef_hauteur), "Terminaison", "white", "center", taille=int(32*coef_hauteur), tag="Terminaison" )
    if Obstacle:
        rectangle(int(625*coef_largeur), int(500*coef_hauteur),int( 925*coef_largeur), int(600*coef_hauteur), "white", "green", 5, tag="Obstacle")
        texte(int(775*coef_largeur), int(550*coef_hauteur), "Obstacle", "white", "center", taille=int(32*coef_hauteur), tag="Obstacle" )
    else:
        rectangle(int(625*coef_largeur), int(500*coef_hauteur),int( 925*coef_largeur), int(600*coef_hauteur), "white", "red", 5, tag="Obstacle")
        texte(int(775*coef_largeur), int(550*coef_hauteur), "Obstacle", "white", "center", taille=int(32*coef_hauteur), tag="Obstacle" )


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
    texte(int(640*coef_largeur), int(80*coef_hauteur), str(round(temps-t1, 1)), "white", "center", taille = int(20*coef_hauteur), tag = "Sablier")
    mise_a_jour()

def fond_score(score):
    texte(int(375*coef_largeur), int(50*coef_hauteur), "Score du Vert : " + str(score[0]), "black", "w", taille = int(20*coef_hauteur), tag = "Scores")
    texte(int(675*coef_largeur), int(50*coef_hauteur), "Score du Violet : " + str(score[1]), "black", "w", taille = int(20*coef_hauteur), tag = "Scores")
    mise_a_jour()

def fleches(direction, x, y):
    rectangle(x, y, x+int(25*coef_largeur), y+int(30*coef_hauteur), "black", "red", tag="Taille")
    if direction == "gauche":
        polygone([x+int(18*coef_largeur), y+int(2*coef_hauteur),x+int(5*coef_largeur), y+int(15*coef_hauteur), x+int( 18*coef_largeur), y+int(28*coef_hauteur)], "darkred", "darkred", tag="Taille")
    else:
        polygone([x+int(7*coef_largeur), y+int(2*coef_hauteur),x+int(20*coef_largeur), y+int(15*coef_hauteur), x+int(7*coef_largeur), y+int(28*coef_hauteur)], "darkred", "darkred", tag="Taille")

def fond_taille():
    texte(int(50*coef_largeur), int(695*coef_hauteur), "Montant à poser:", "black", "w", taille=int(20*coef_hauteur), tag="Taille")
    # Centaines
    fleches("gauche", int(260*coef_largeur), int(680*coef_hauteur))
    fleches("droite", int(320*coef_largeur), int(680*coef_hauteur))
    rectangle(int(290*coef_largeur), int(680*coef_hauteur), int(315*coef_largeur), int(710*coef_hauteur), "darkcyan", "floralwhite", tag="Taille")
    texte(int(303*coef_largeur), int(695*coef_hauteur), "0", "black", "center", taille=int(24*coef_hauteur), tag="centaine")
    # Dizanes
    fleches("gauche", int(360*coef_largeur), int(680*coef_hauteur))
    fleches("droite", int(420*coef_largeur), int(680*coef_hauteur))
    rectangle(int(390*coef_largeur), int(680*coef_hauteur), int( 415*coef_largeur), int(710*coef_hauteur), "darkcyan", "floralwhite", tag="Taille")
    texte(int(403*coef_largeur), int(695*coef_hauteur), "0", "black", "center", taille=int(24*coef_hauteur), tag="dizaine")
    # Unites
    fleches("gauche", int(460*coef_largeur), int(680*coef_hauteur))
    fleches("droite", int(520*coef_largeur), int(680*coef_hauteur))
    rectangle(int(490*coef_largeur), int(680*coef_hauteur), int( 515*coef_largeur), int(710*coef_hauteur), "darkcyan", "floralwhite", tag="Taille")
    texte(int(503*coef_largeur), int(695*coef_hauteur), "0", "black", "center", taille=int(24*coef_hauteur), tag="unite")
    mise_a_jour()

def epargne_joueurs(epargne_Vert, epargne_Violet):
    efface("epargne")
    texte(int(600*coef_largeur), int(695*coef_hauteur), "Montant Vert:" + str(epargne_Vert), "black", "w", taille=int(20*coef_hauteur), tag="epargne")
    texte(int(850*coef_largeur), int(695*coef_hauteur), "Montant Violet:" + str(epargne_Violet), "black", "w", taille=int(20*coef_hauteur), tag="epargne")

def variante_sablier():
    """ 
    Renvoie les coordonnées du clic et fait appliquer au programme la variante 'Sablier' 
    si elle a été sélectionnée dans le menu.
    """
    temps=time() + 10
    while time() < temps:
        ev = donne_evenement()
        mise_a_jour()
        type_ev = type_evenement(ev)
        fond_sablier(temps, time())
        if type_ev == "ClicGauche":
            x, y = clic_x(ev), clic_y(ev)
            if int(1130*coef_largeur) <= x <= int(1230*coef_largeur) and int(680*coef_hauteur) <=y<= int(715*coef_hauteur):
                return x, y
            if x < int(50*coef_largeur) or x > int(1230*coef_largeur) or y < int(100*coef_hauteur) or y > int(670*coef_hauteur):
                continue
            return x, y
    return False, False

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
    texte(int(303*coef_largeur), int(695*coef_hauteur), str(centaine), "black", "center", taille=int(24*coef_hauteur), tag="centaine")
    texte(int(403*coef_largeur), int(695*coef_hauteur), str(dizaine), "black", "center", taille=int(24*coef_hauteur), tag="dizaine")
    texte(int(503*coef_largeur), int(695*coef_hauteur), str(unite), "black", "center", taille=int(24*coef_hauteur), tag="unite")
    mise_a_jour()
    return centaine, dizaine, unite

def variante_terminaison(numero_tour):
    nb_max_tour = numero_tour + 5
    return nb_max_tour

######################## Fonctions de detection ##################################################################################

def detection_variante(Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter):
    while True:
        x, y, z = attente_clic()
        if int(490*coef_largeur) <= x <= int(790*coef_largeur) :
            if int(200*coef_hauteur) <= y <= int(300*coef_hauteur):
                efface("Menu")
                fond_jeu()
                break
            elif int(350*coef_hauteur) <= y <= int(450*coef_hauteur):
                efface("Menu")
                variantes(Sablier, Scores, Taille, Dynamique, Terminaison, Obstacle)
                while True:
                    x, y, z = attente_clic()
                    if int(275*coef_largeur) <= x <= int(575*coef_largeur) and int(200*coef_hauteur) <= y <= int(300*coef_hauteur):
                        if Sablier == False :
                            efface("Sablier")
                            rectangle(int(275*coef_largeur), int(200*coef_hauteur) ,int(575*coef_largeur), int(300*coef_hauteur), "white", "green", 5, tag="Sablier")
                            texte(int(425*coef_largeur), int(250*coef_hauteur), "Sablier", "white", "center", taille=int(32*coef_hauteur), tag="Sablier")
                            mise_a_jour()
                            Sablier = True
                        else:
                            efface("Sablier")
                            rectangle(int(275*coef_largeur), int(200*coef_hauteur), int(575*coef_largeur), int(300*coef_hauteur), "white", "red", 5, tag="Sablier")
                            texte(int(425*coef_largeur), int(250*coef_hauteur), "Sablier", "white", "center", taille=int(32*coef_hauteur), tag="Sablier")
                            mise_a_jour()
                            Sablier = False
                    elif int(625*coef_largeur) <= x <= int(925*coef_largeur) and int(200*coef_hauteur) <= y <= int(300*coef_hauteur):
                        if not Scores:
                            efface("Scores")
                            rectangle(int(625*coef_largeur), int(200*coef_hauteur), int(925*coef_largeur), int(300*coef_hauteur), "white", "green", 5, tag="Scores")
                            texte(int(775*coef_largeur), int(250*coef_hauteur), "Scores", "white", "center", taille=int(32*coef_hauteur), tag="Scores")
                            mise_a_jour()
                            Scores = True
                        else:
                            efface("Scores")
                            rectangle(int(625*coef_largeur), int(200*coef_hauteur), int( 925*coef_largeur), int(300*coef_hauteur), "white", "red", 5, tag="Scores")
                            texte(int(775*coef_largeur), int(250*coef_hauteur), "Scores", "white", "center", taille=int(32*coef_hauteur), tag="Scores")
                            mise_a_jour()
                            Scores = False
                    elif int(275*coef_largeur) <= x <= int(575*coef_largeur) and int(350*coef_hauteur) <= y <= int(450*coef_hauteur):
                        if not Taille:
                            efface("Taille")
                            rectangle(int(275*coef_largeur), int(350*coef_hauteur), int(575*coef_largeur), int(450*coef_hauteur), "white", "green", 5, tag="Taille")
                            texte(int(425*coef_largeur), int(400*coef_hauteur), "Taille", "white", "center", taille=int(32*coef_hauteur), tag="Taille" )
                            mise_a_jour()
                            Taille = True
                        else:
                            efface("Taille")
                            rectangle(int(275*coef_largeur), int(350*coef_hauteur), int(575*coef_largeur), int(450*coef_hauteur), "white", "red", 5, tag="Taille")
                            texte(int(425*coef_largeur), int(400*coef_hauteur), "Taille", "white", "center", taille=int(32*coef_hauteur), tag="Taille" )
                            mise_a_jour()
                            Taille = False
                    elif int(625*coef_largeur) <= x <= int(925*coef_largeur) and int(350*coef_hauteur) <= y <= int(450*coef_hauteur):
                        if not Dynamique:
                            efface("Dynamique")
                            rectangle(int(625*coef_largeur), int(350*coef_hauteur) ,int(925*coef_largeur), int(450*coef_hauteur), "white", "green", 5, tag="Dynamique")
                            texte(int(775*coef_largeur), int(400*coef_hauteur), "Dynamique", "white", "center", taille=int(32*coef_hauteur), tag="Dynamique" )
                            mise_a_jour()
                            Dynamique = True
                        else:
                            efface("Dynamique")
                            rectangle(int(625*coef_largeur), int(350*coef_hauteur), int( 925*coef_largeur), int(450*coef_hauteur), "white", "red", 5, tag="Dynamique")
                            texte(int(775*coef_largeur), int(400*coef_hauteur), "Dynamique", "white", "center", taille=int(32*coef_hauteur), tag="Dynamique" )
                            mise_a_jour()
                            Dynamique = False
                    elif int(275*coef_largeur) <= x <= int(575*coef_largeur) and int(500*coef_hauteur) <= y <= int(600*coef_hauteur):
                        if Terminaison == False :
                            efface("Terminaison")
                            rectangle(int(275*coef_largeur), int(500*coef_hauteur), int(575*coef_largeur), int(600*coef_hauteur), "white", "green", 5, tag="Terminaison")
                            texte(int(425*coef_largeur), int(550*coef_hauteur), "Terminaison", "white", "center", taille=int(32*coef_hauteur), tag="Terminaison" )
                            mise_a_jour()
                            Terminaison = True
                        else:
                            efface("Terminaison")
                            rectangle(int(275*coef_largeur), int(500*coef_hauteur), int(575*coef_largeur), int(600*coef_hauteur), "white", "red", 5, tag="Terminaison")
                            texte(int(425*coef_largeur), int(550*coef_hauteur), "Terminaison", "white", "center", taille=int(32*coef_hauteur), tag="Terminaison" )
                            mise_a_jour()
                            Terminaison = False
                    elif int(625*coef_largeur) <= x <= int(925*coef_largeur) and int(500*coef_hauteur) <= y <= int(600*coef_hauteur):
                        if not Obstacle:
                            efface("Obstacle")
                            rectangle(int(625*coef_largeur), int(500*coef_hauteur), int( 925*coef_largeur), int(600*coef_hauteur), "white", "green", 5, tag="Obstacle")
                            texte(int(775*coef_largeur), int(550*coef_hauteur), "Obstacle", "white", "center", taille=int(32*coef_hauteur), tag="Obstacle" )
                            mise_a_jour()
                            Obstacle = True
                        else:
                            efface("Obstacle")
                            rectangle(int(625*coef_largeur), int(500*coef_hauteur), int(925*coef_largeur), int(600*coef_hauteur), "white", "red", 5, tag="Obstacle")
                            texte(int(775*coef_largeur), int(550*coef_hauteur), "Obstacle", "white", "center", taille=int(32*coef_hauteur), tag="Obstacle" )
                            mise_a_jour()
                            Obstacle = False
                    elif int(1130*coef_largeur) <=x<= int(1230*coef_largeur) and int(680*coef_hauteur) <=y<=int(715*coef_hauteur):
                        efface("Variante")
                        efface("Sablier")
                        efface("Scores")
                        efface("Taille")
                        efface("Dynamique")
                        efface("Terminaison")
                        efface("Obstacle")
                        fond_menu()
                        mise_a_jour()
                        break
            elif int(500*coef_hauteur) <= y <= int(600*coef_hauteur):
                ferme_fenetre()
                Quitter = True
                break
    return Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter

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

def detection_tour(tour, listeJoueur, numero_tour, nb_max_tour):
    """ 
    Affiche les textes indiquant à qui est le tour et le nombre de tour que les joueurs ont effectués où :
    tour : indique à quel joueur c'est au tour de jouer (paramètre : int) (valeur : '0' ou '1' pour respectivement Joueur 1 ou Joueur 2)
    listeJoueur : indique la liste des joueurs qui jouent (paramètre : str)
    numero_tour : indique le nombre de tours joués (paramètre : int)
    nb_max_tour : indique le nombre maximum de tours (paramètre : int)
    """
    efface("tour")
    texte(int(50*coef_largeur), int(50*coef_hauteur), "Tour : " + listeJoueur[tour], "lightcyan", "w", taille=int(24*coef_hauteur), tag="tour")
    texte(int(1230*coef_largeur), int(50*coef_hauteur), "Tour n° "+ str(numero_tour) + "/"+str(nb_max_tour), "lightcyan", "e", taille=int(24*coef_hauteur), tag="tour")

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

def scinder(x, y, liste_cercle_violet, liste_cercle_vert, element, distance, tour, couleurJoueur):
    """
    Permet la division des cercles lorsque un joueur clique sur le cercle adverse.
    x, y (float/int) : cordonnées x et y du clic du joueur dans le terrain de jeu
    liste_cercle_vert (list) : liste contenant les informations sur les différents cercle du joueur vert sur le terrain
    liste_cercle_violet (list) : liste contenant les informations sur les différents cercle du joueur violet sur le terrain
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

    tag1 = cercle(x, y, rayon1, "black", couleurJoueur[tour], 1)
    tag2 = cercle(x2, y2, rayon2, "black", couleurJoueur[tour], 1)
    if tour == 0:
        liste_cercle_vert.append([x, y, rayon1, tag1])
        liste_cercle_vert.append([x2, y2, rayon2, tag2])
        liste_cercle_vert.pop(liste_cercle_vert.index(element))
    else:
        liste_cercle_violet.append([x2, y2, rayon2, tag2])  
        liste_cercle_violet.append([x, y, rayon1, tag1])
        liste_cercle_violet.pop(liste_cercle_violet.index(element))
    efface(element[3])

def cerkle(x, y, couleur, liste_cercle_vert, liste_cercle_violet, rayon):
    """
    Cette fonction permet d'afficher les cercles et les intègre dans une liste pour garder les différentes informations tel que :
    x, y : cordonnées x et if 50<=x<100:
                x=100
            elif 1180<x<=1230:
                x=1180
                
            if 100<=y<150:
                y=150
            elif 620<y<=670:
                y=620, id_cercle]
    rayon : indique le rayon du cercle prochainement généré
    """
    id_cercle = cercle(x, y, rayon, "black", couleur, 1)
    if couleur == "mediumseagreen":
        liste_cercle_vert.append([x, y, rayon, id_cercle])
    else:
        liste_cercle_violet.append([x, y, rayon, id_cercle])

def main():
    cree_fenetre(largeur_fenetre, hauteur_fenetre)
    rectangle(-1,-1, largeur_fenetre, hauteur_fenetre,"darkcyan","darkcyan")
    fond_menu()
    Sablier = False
    Scores = False
    Terminaison = False
    Taille = False
    Dynamique = False
    Obstacle = False
    Quitter = False
    
    Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter = detection_variante(Sablier, Scores, Terminaison, Taille, Dynamique, Obstacle, Quitter)

    if Quitter == False:
        # Variables
        listeJoueur = ["Joueur Vert","Joueur Violet"]
        couleurJoueur = ["mediumseagreen", "mediumpurple"]
        liste_cercle_violet = []
        liste_cercle_vert = []
        tour, numero_tour = 0, 1
        rayon = int(50*coef_largeur)
        nb_max_tour = 10
        score=[0, 0]
        inter = 0
        alterner_liste_joueur, b = liste_cercle_violet, liste_cercle_vert
        detection_terminaison = 0
        # Variante taille de boule
        if Taille:
            centaine = 0
            dizaine = 0
            unite = 0
            fond_taille()
            epargne_vert = int(100*coef_largeur)
            epargne_violet = int(100*coef_largeur)
            epargne_joueurs(epargne_vert, epargne_violet)
        while numero_tour < nb_max_tour+1:
            x = None
            detection_tour(tour, listeJoueur, numero_tour, nb_max_tour)
            if Sablier:
                t = 0
                temps = time() + 10
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
                        if Scores and touche(ev) == 's':
                            x, y, t = variante_score(score, t)
                            if x != None:
                                break
                            continue
                        if Terminaison and detection_terminaison == 0 and touche(ev) == 't':
                            nb_max_tour = variante_terminaison(numero_tour)
                            detection_terminaison += 1
                            if x != None:
                                break
                            continue
                if x == None:
                    if tour == 1:
                        numero_tour += 1
                    tour = (tour+1) % 2
                    mise_a_jour()
                    continue
            elif Scores:
                ev = donne_evenement()
                mise_a_jour()
                type_ev = type_evenement(ev)
                if type_ev == 'ClicGauche':
                    x, y = clic_x(ev), clic_y(ev)
                elif type_ev == 'Touche':
                    if touche(ev) == 's':
                        x, y = variante_score(score, None) 
                        if x == None:
                            continue
                    elif Terminaison and detection_terminaison == 0 and touche(ev) == 't':
                        nb_max_tour = variante_terminaison(numero_tour)
                        detection_terminaison += 1
                        if x != None:
                            break
                        continue
                    else:
                        continue
                else:
                    continue

            elif Terminaison and detection_terminaison == 0:
                ev = donne_evenement()
                mise_a_jour()
                type_ev = type_evenement(ev)
                if type_ev == 'ClicGauche':
                    x, y = clic_x(ev), clic_y(ev)
                elif type_ev == 'Touche':
                    if touche(ev) == 't':
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
                        if epargne_vert - depense < 0:
                            continue
                        else:
                            epargne_vert -= depense
                            rayon = depense
                    else:
                        if epargne_violet - depense < 0:
                            continue
                        else:
                            epargne_violet -= depense
                            rayon = depense
                    epargne_joueurs(epargne_vert, epargne_violet)

            x, y = clic_hors_bordure(x, y)
            if int(1130*coef_largeur) <= x <= int(1230*coef_largeur) and int(680*coef_hauteur) <= y <= int(715*coef_hauteur):
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
                    scinder(x, y, alterner_liste_joueur, liste_cercle_vert, element, distance, tour, couleurJoueur)
                    intersection_cercle += 1
                    
            alterner_liste_joueur, b = b, alterner_liste_joueur

            if intersection_cercle == 0 and rayon != 0:
                cerkle(x, y, couleurJoueur[tour], liste_cercle_vert, liste_cercle_violet, rayon)

                detection_cercle_inscrit(alterner_liste_joueur)

                if tour == 0 and inter!= 0:
                    intersection_vert = inter
                elif tour == 1 and inter!=0:
                    intersection_violet = inter

            score[0] = len(calcul_score(liste_cercle_vert))
            score[1] = len(calcul_score(liste_cercle_violet))
            if numero_tour == nb_max_tour+1 and tour == 1:
                if score[0] > score[1]:
                    texte(int(640*coef_largeur), int(50*coef_hauteur),"Le Joueur Vert gagne", "white", "center",  taille=int(24*coef_hauteur))
                    attente_clic()
                elif score[1] > score[0]:
                    texte(int(640*coef_largeur), int(50*coef_hauteur), "Le Joueur Violet gagne", "white", "center",  taille=int(24*coef_hauteur))
                    attente_clic()
                else:
                    texte(int(640*coef_largeur), int(50*coef_hauteur), "Egalité", "white", "center", taille=int(24*coef_hauteur))
                    attente_clic()
                        
            tour = (tour+1) % 2 

            mise_a_jour()
        ferme_fenetre()

if __name__ == '__main__':
    main()
