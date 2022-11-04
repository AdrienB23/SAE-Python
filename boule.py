from upemtk import *
from random import *
from time import *
from math import *

def fond(): 
    cree_fenetre(1280, 720)
    rectangle(-1,-1,1280,720,"darkcyan","darkcyan")
    rectangle(50,100,1280-50,720-50,"floralwhite","floralwhite")

def detection_tour(tour, listeJoueur, numero_tour):
    efface("tour")
    texte(50, 50,"Tour : " + listeJoueur[tour],"lightcyan", "w",police="",tag="tour")
    texte(1280-50, 50, "Tour n° "+ str(numero_tour) + "/20", "lightcyan","e",police="",tag="tour")

def cerkle(x, y, couleurJoueur, tour, liste_cercle, rayon):
    tag = cercle(x, y, rayon, couleurJoueur[tour], couleurJoueur[tour])
    liste_cercle.append([x, y, rayon, tag, tour])

# def actualiser_score(scores):
#     efface("tour2")
#     texte(25,720-25,"Score Joueur 1 : " + str(scores[0]), "lightcyan","w",taille=16,tag="tour2")
#     texte(1280-25,720-25,"Score Joueur 2 : " + str(scores[1]), "lightcyan","e",taille=16,tag="tour2")
#     pass

def main():
    # LargeurFenetre = 1280, HauteurFenetre = 720, tailleTerrain = 50
    listeJoueur = ["Joueur 1","Joueur 2"]
    couleurJoueur = ["mediumseagreen", "mediumpurple"]
    scores = [0, 0]
    fond()

    liste_cercle = []
    tour, numero_tour = 0, 1
    texte(0,0,"",tag="tour")
    texte(0,0,"",tag="tour2")

    rayon = 50

    while True:
        ev = donne_evenement()
        type_ev = type_evenement(ev)

        detection_tour(tour, listeJoueur, numero_tour)

        #actualiser_score(scores)

        if type_ev == "ClicGauche":
            x, y = clic_x(ev), clic_y(ev)
            if tour == 1:
                numero_tour += 1

            intersection_cercle = 0
            intersection_bord = 0
            for element in liste_cercle:
                distance = (x-element[0])**2 + (y-element[1])**2
                if sqrt(distance) < element[2]+rayon and sqrt(distance) > element[2] and element[4] != tour:
                    intersection_cercle += 1
                elif sqrt(distance) < element[2] and element[4] != tour:
                    intersection_cercle += 1

            if intersection_cercle == 0 and 50<=x<=1280-50 and 100<=y<=720-50:
                cerkle(x, y, couleurJoueur, tour, liste_cercle, rayon)

                #scores[tour] += round(pi*(rayon**2))

            tour = (tour+1) % 2

        if type_ev == "Quitte" or numero_tour == 21:
            break   

        mise_a_jour()

    ferme_fenetre()

if __name__ == '__main__':
    main()