from upemtk import *
from random import *
from time import *
from math import *

def fond_menu():
    rectangle(2, 2, 1277, 150, "white", epaisseur=5, tag="Menu")
    texte(640, 75, "Bataille des boules", "white", "center", taille=50, tag="Menu")

    rectangle(490, 250, 790, 350, "white", "#009382", 5, tag="Menu")
    texte(640, 300, "Jouer", "white", "center", taille=40, tag="Menu")

    rectangle(490, 400, 790, 500, "white", "#009382", 5, tag="Menu")
    texte(640, 450, "Options", "white", "center", taille=40, tag="Menu")
    mise_a_jour() 

def fond_jeu(): 
    rectangle(50,100,1280-50,720-50,"floralwhite","floralwhite")

    rectangle(1130, 680, 1230, 715, "black","red", 1, "Quitter")
    texte(1143, 685, "Quitter", "white", "nw", taille="16")

    texte(0,0,"",tag="tour")
    texte(0,0,"",tag="tour2")
    mise_a_jour()

def options():
    efface("Options")
    rectangle(2, 2, 1277, 150, "white", epaisseur=5, tag="Options")
    texte(640, 75, "Options", "white", "center", taille=50, tag="Options")

    rectangle(250, 200, 550, 300, "white", "red", 5, tag="Sablier")
    texte(400, 250, "Sablier", "white", "center", taille=40, tag="Sablier")

    rectangle(1130, 680, 1230, 715, "black","red", 1, "Options")
    texte(1143, 685, "Retour", "white", "nw", taille="16", tag="Options")
    mise_a_jour()

def fond_sablier(temps, t1):
    efface("Temps")
    texte(640, 80, str(round(temps-t1, 1)), "white", "center", taille = 20, tag = "Temps")
    mise_a_jour()

def clique(Sablier):
    if Sablier:
        temps=time() + 5
        t1 = time()
        while t1 < temps:
            ev = donne_evenement()
            type_ev = type_evenement(ev)
            t1 = time()
            fond_sablier(temps, t1)
            if type_ev == "ClicGauche":
                x, y = clic_x(ev), clic_y(ev)
                if 1130<=x<=1230 and 680<=y<=715:
                    return True, True
                if x<50 or x>1230 or y<100 or y>670:
                    continue
                return x, y
        return False, False
    else:
        x, y, w = attente_clic()
        return x, y

def clic_hors_bordure(x, y):
    while x<50 or x>1230 or y<100 or y>670:
        x, y, m = attente_clic()
    return x, y

def detection_tour(tour, listeJoueur, numero_tour, nb_max_tour):
    efface("tour")
    texte(50, 50,"Tour : " + listeJoueur[tour],"lightcyan", "w",police="",tag="tour")
    texte(1280-50, 50, "Tour n° "+ str(numero_tour) + "/"+str(nb_max_tour), "lightcyan","e",police="",tag="tour")

def scinder(x, y, liste_cercle_violet, liste_cercle_vert, element, distance, tour, couleurJoueur):
    tour = (tour+1) % 2
    rayon1 = element[2]-sqrt(distance)
    rayon2 = element[2]-rayon1
    
    if x - element[0] == 0:
        m2 = x
    else:
        m2 = (y-element[1])/(x-element[0])
    m3 = 0
    calcul = abs((m2-m3)/(1+m3*m2))
    gamma = atan(calcul) * (180/pi)
    alpha = (90-gamma) * (pi/180)
    x2 = sin(alpha)*rayon1
    y2 = cos(alpha)*rayon1
    if element[0]-x < 0:
        x2 = element[0]-x2
    else:
        x2 = element[0]+x2
    if element[1]-y < 0:
        y2 = element[1]-y2
    else:
        y2 = element[1]+y2

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
    circle = cercle(x, y, rayon, "black", couleur, 1)
    if couleur == "mediumseagreen":
        liste_cercle_vert.append([x, y, rayon, circle])
    else:
        liste_cercle_violet.append([x, y, rayon, circle])

def calcul_score(a, b, score, tour):
    for i in range(len(a)-1, -1, -1):
        element=a[i]
        score[tour] += ( element[2]**2 * pi )

def main():
    cree_fenetre(1280, 720)
    rectangle(-1,-1,1280,720,"darkcyan","darkcyan")
    fond_menu()
    Sablier = False
    while True:
        x, y, z = attente_clic()
        if 490<=x<=790 and 250<=y<=350:
            efface("Menu")
            fond_jeu()
            break
        elif 490<=x<=790 and 400<=y<=500:
            efface("Menu")
            options()
            while True:
                x, y, z = attente_clic()
                if 250<=x<=550 and 200<=y<=300:
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
                elif 1130<=x<=1230 and 680<=y<=715:
                    efface("Options")
                    efface("Sablier")
                    fond_menu()
                    mise_a_jour()
                    break
    
    listeJoueur = ["Joueur 1","Joueur 2"]
    couleurJoueur = ["mediumseagreen", "mediumpurple"]
    liste_cercle_violet = []
    liste_cercle_vert = []
    tour, numero_tour = 0, 1
    rayon = 50
    nb_max_tour = 5
    score=[0, 0]
    a, b = liste_cercle_violet, liste_cercle_vert
    
    while numero_tour < nb_max_tour+1:
        x, y = clique(Sablier)
        detection_tour(tour, listeJoueur, numero_tour, nb_max_tour)
        if x == False:
            if tour == 1:
                numero_tour += 1
            tour = (tour+1) % 2
            mise_a_jour()
            continue
        if x == True or (1130<=x<=1230 and 680<=y<=715):
            break

        clic_hors_bordure(x, y)

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

        for i in range(len(a)-1, -1, -1):
            element = a[i]
            distance = (x-a[i][0])**2 + (y-a[i][1])**2
            if sqrt(distance) < a[i][2] + rayon and sqrt(distance) > a[i][2]:
                intersection_cercle += 1
            elif sqrt(distance) < a[i][2]:
                scinder(x, y, a, liste_cercle_vert, element, distance, tour, couleurJoueur)
                intersection_cercle += 1
                break
        a, b = b, a

        if intersection_cercle == 0:
            cerkle(x, y, couleurJoueur[tour], liste_cercle_vert, liste_cercle_violet, rayon)

        calcul_score(a, b, score, tour)
        score[0] = round(score[0])
        score[1] = round(score[1])

        if numero_tour == 6 and tour == 1:
            if score[0] > score[1]:
                texte(640, 50, "Le Joueur Vert gagne", "white", "center")
                attente_clic()
            elif score[1] < score[0]:
                texte(640, 50, "Le Joueur Violet gagne", "white", "center")
                attente_clic()
            else:
                texte(640, 50, "Egalité", "white", "center")
                attente_clic()
                    
        tour = (tour+1) % 2 

        mise_a_jour()

    ferme_fenetre()

if __name__ == '__main__':
    main()
