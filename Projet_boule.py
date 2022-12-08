from upemtk import *
from random import *
from time import *
from math import *

######################## Fonction d'aspect graphique des différents affichages ###################################################

def fond_menu(): # Affiche le menu du jeu
    rectangle(2, 2, 1277, 150, "white", epaisseur=5, tag="Menu")
    texte(640, 75, "Bataille des boules", "white", "center", taille=50, tag="Menu")

    rectangle(490, 200, 790, 300, "white", "#009382", 5, tag="Menu")
    texte(640, 250, "Jouer", "white", "center", taille=40, tag="Menu")

    rectangle(490, 350, 790, 450, "white", "#009382", 5, tag="Menu")
    texte(640, 400, "Variantes", "white", "center", taille=40, tag="Menu")

    rectangle(490, 500, 790, 600, "white", "#009382", 5, tag="Menu")
    texte(640, 550, "Quitter", "white", "center", taille=40, tag="Menu")
    mise_a_jour() 

def fond_jeu(): # Affiche les éléments du terrains de jeu
    rectangle(50, 100, 1230, 670,"floralwhite","floralwhite")

    rectangle(1130, 680, 1230, 715, "black","red", 1, "Quitter")
    texte(1180, 698, "Quitter", "white", "c", taille="16")

    texte(0,0,"",tag="tour")
    texte(0,0,"",tag="tour2")
    mise_a_jour()

def variantes(Sablier, Scores): # Affiche le menu des variantes pour choisir une ou plusieurs variantes (pour l'instant seul le sablier est disponible)
    efface("Variante")
    rectangle(2, 2, 1277, 150, "white", epaisseur=5, tag="Variante")
    texte(640, 75, "Variantes", "white", "center", taille=50, tag="Variante")
    if Sablier:
        rectangle(250, 200, 550, 300, "white", "green", 5, tag="Sablier")
        texte(400, 250, "Sablier", "white", "center", taille=40, tag="Sablier")
    else:
        rectangle(250, 200, 550, 300, "white", "red", 5, tag="Sablier")
        texte(400, 250, "Sablier", "white", "center", taille=40, tag="Sablier")
    if Scores:
        rectangle(600, 200, 900, 300, "white", "green", 5, tag="Scores")
        texte(750, 250, "Scores", "white", "center", taille=40, tag="Scores" )
    else:
        rectangle(600, 200, 900, 300, "white", "red", 5, tag="Scores")
        texte(750, 250, "Scores", "white", "center", taille=40, tag="Scores" )

    rectangle(1130, 680, 1230, 715, "black","red", 1, "Variante")
    texte(1143, 685, "Retour", "white", "nw", taille="16", tag="Variante")
    mise_a_jour()

######################## Fonctions d'ajout et de choix des variants/option #######################################################

def fond_sablier(temps, t1):
    """ 
    Affiche un temps qui s'écoule où 'temps' est le temps maximum que doit prendre un jouer pour jouer
    et 't1' le temps qui augmente tant que le joueur ne joue pas.
    """
    efface("Sablier")
    texte(640, 80, str(round(temps-t1, 1)), "white", "center", taille = 20, tag = "Sablier")
    mise_a_jour()

def fond_score(score):
    texte(325, 50, "Score du Vert : " + str(score[0]), "mediumseagreen", "w", taille = 30, tag = "Scores")
    texte(700, 50, "Score du Violet : " + str(score[1]), "mediumpurple", "w", taille = 30, tag = "Scores")
    mise_a_jour()   

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
            if 1130<=x<=1230 and 680<=y<=715:
                return x, y
            if x<50 or x>1230 or y<100 or y>670:
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

######################## Fonctions de detection ##################################################################################

def clic_hors_bordure(x, y):
    """ 
    Redemande au joueur de cliquer dans la zone lorsque les coordonnées 'x' et 'y' ne sont pas respectées.
    """
    while x<50 or x>1230 or y<100 or y>670:
        x, y, m = attente_clic()
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
    texte(50, 50,"Tour : " + listeJoueur[tour], "lightcyan", "w", tag="tour")
    texte(1280-50, 50, "Tour n° "+ str(numero_tour) + "/"+str(nb_max_tour), "lightcyan", "e", tag="tour")

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
    x, y : cordonnées x et y du clic du joueur dans le terrain de jeu
    couleur : permet de récuperer la couleur du joueur
    liste_cercle_vert : liste contenant les informations sur les différents cercle du joueur vert sur le terrain, nécessaire lors de l'ajout d'un nouveau cercle
    liste_cercle_violet : liste contenant les informations sur les différents cercle du joueur violet sur le terrain
    Les différentes informations sur les cercles sont stocké dans ces deux précédentes listes et sont de la forme :
    un cercle = [x, y, rayon, id_cercle]
    rayon : indique le rayon du cercle prochainement généré
    """
    id_cercle = cercle(x, y, rayon, "black", couleur, 1)
    if couleur == "mediumseagreen":
        liste_cercle_vert.append([x, y, rayon, id_cercle])
    else:
        liste_cercle_violet.append([x, y, rayon, id_cercle])

def main():
    cree_fenetre(1280, 720)
    rectangle(-1,-1,1280,720,"darkcyan","darkcyan")
    fond_menu()
    Sablier = False
    Scores = False
    Quitter = False
    while True:
        x, y, z = attente_clic()
        if 490 <= x <= 790: 
            if 200 <= y <= 300:
                efface("Menu")
                fond_jeu()
                break
            elif 350 <= y <= 450:
                efface("Menu")
                variantes(Sablier, Scores)
                while True:
                    x, y, z = attente_clic()
                    if 250 <= x <= 550 and 200 <= y <= 300:
                        if Sablier == False :
                            efface("Sablier")
                            rectangle(250, 200, 550, 300, "white", "green", 5, tag="Sablier")
                            texte(400, 250, "Sablier", "white", "center", taille=40, tag="Sablier")
                            mise_a_jour()
                            Sablier = True
                        else:
                            efface("Sablier")
                            rectangle(250, 200, 550, 300, "white", "red", 5, tag="Sablier")
                            texte(400, 250, "Sablier", "white", "center", taille=40, tag="Sablier")
                            mise_a_jour()
                            Sablier = False
                    elif 600 <= x <= 900 and 200 <= y <= 300:
                        if not Scores:
                            efface("Scores")
                            rectangle(600, 200, 900, 300, "white", "green", 5, tag="Scores")
                            texte(750, 250, "Scores", "white", "center", taille=40, tag="Scores" )
                            mise_a_jour()
                            Scores = True
                        else:
                            efface("Scores")
                            rectangle(600, 200, 900, 300, "white", "red", 5, tag="Scores")
                            texte(750, 250, "Scores", "white", "center", taille=40, tag="Scores" )
                            mise_a_jour()
                            Scores = False
                    elif 1130<=x<=1230 and 680<=y<=715:
                        efface("Variante")
                        efface("Sablier")
                        efface("Scores")
                        fond_menu()
                        mise_a_jour()
                        break
            elif 500 <= y <=600:
                ferme_fenetre()
                Quitter = True
                break

    if Quitter == False:
        listeJoueur = ["Joueur Vert","Joueur Violet"]
        couleurJoueur = ["mediumseagreen", "mediumpurple"]
        liste_cercle_violet = []
        liste_cercle_vert = []
        tour, numero_tour = 0, 1
        rayon = 50
        nb_max_tour = 5
        score=[0, 0]
        inter, intersection_vert, intersection_violet = 0, 0, 0
        alterner_liste_joueur, b = liste_cercle_violet, liste_cercle_vert

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
                        if 1130<=x<=1230 and 680<=y<=715:
                            break
                        if x<50 or x>1230 or y<100 or y>670:
                            continue
                        break
                    elif type_ev == "Touche":
                        if Scores and touche(ev) == 's':
                            x, y, t = variante_score(score, t)
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
                    else:
                        continue        
                else:
                    continue
            
            if x == None:
                x, y, w = attente_clic()
            
            if 1130<=x<=1230 and 680<=y<=715:
                break

            x, y = clic_hors_bordure(x, y)

            if 50<=x<100:
                x=100
            elif 1180<x<=1230:
                x=1180
                
            if 100<=y<150:
                y=150
            elif 620<y<=670:
                y=620

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
                    break
            alterner_liste_joueur, b = b, alterner_liste_joueur

            if intersection_cercle == 0:
                cerkle(x, y, couleurJoueur[tour], liste_cercle_vert, liste_cercle_violet, rayon)

                detection_cercle_inscrit(alterner_liste_joueur)

                if tour == 0 and inter!= 0:
                    intersection_vert = inter
                elif tour == 1 and inter!=0:
                    intersection_violet = inter

            score[0] = len(calcul_score(liste_cercle_vert))
            score[1] = len(calcul_score(liste_cercle_violet))
            if numero_tour == 6 and tour == 1:
                if score[0] > score[1]:
                    texte(640, 50, "Le Joueur Vert gagne", "white", "center")
                    attente_clic()
                elif score[1] > score[0]:
                    texte(640, 50, "Le Joueur Violet gagne", "white", "center")
                    attente_clic()
                else:
                    texte(640, 50, "Egalité", "white", "center")
                    attente_clic()
                        
            tour = (tour+1) % 2 

            mise_a_jour()
        print(score)
        ferme_fenetre()

if __name__ == '__main__':
    main()
