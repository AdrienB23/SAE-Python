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

def cerkle(x, y, couleur, liste_cercle_vert, liste_cercle_violet, rayon):
    circle = cercle(x, y, rayon, "black", couleur, 1)
    if couleur == "mediumseagreen":
        liste_cercle_vert.append([x, y, rayon, circle])
    else:
        liste_cercle_violet.append([x, y, rayon, circle])

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

    liste_cercle_violet = []
    liste_cercle_vert = []
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
            x, y = attente_clic()
            while x<50 or x>1230 or y<100 or y>670:
                x, y = attente_clic()
            
            if 50<=x<100:
                x=100
            elif 1170<x<=1230:
                x=1170
            if 100<=y<150:
                y=150
            elif 620<y<=570:
                y=20
        
            if tour == 1:
                numero_tour += 1
        
            intersection_cercle = 0

        
#---------Division des cercles rouges---------#

            if listeJoueur[tour] == "Joueur 1":
                for i in range(len(liste_cercle_violet)):
                    element = liste_cercle_violet[i]
                    distance = (x-liste_cercle_violet[i][0])**2 + (y-liste_cercle_violet[i][1])**2
                    if sqrt(distance) < liste_cercle_violet[i][2] + rayon and sqrt(distance) > liste_cercle_violet[i][2]:
                        intersection_cercle += 1
                    elif sqrt(distance) < liste_cercle_violet[i][2]:
                        scinder("red") #A modifier
                        intersection_cercle += 1
                        break
                    
#---------Division des cercles verts---------#

            if listeJoueur[tour] == "Joueur 2":
                for i in range(len(liste_cercle_vert)):
                    element = liste_cercle_vert[i]
                    distance = (x-liste_cercle_vert[i][0])**2 + (y-liste_cercle_vert[i][1])**2
                    if sqrt(distance) < liste_cercle_vert[i][2] + rayon and sqrt(distance) > liste_cercle_vert[i][2]:
                        intersection_cercle += 1
                    elif sqrt(distance) < liste_cercle_vert[i][2]:
                        scinder("lime") # A modifier
                        intersection_cercle += 1
                        break


            if intersection_cercle == 0:
                cerkle(x, y, couleurJoueur[tour], liste_cercle_vert, liste_cercle_violet, rayon)

                #scores[tour] += round(pi*(rayon**2))

            tour = (tour+1) % 2

        if type_ev == "Quitte" or numero_tour == 21:
            break   

        mise_a_jour()

    ferme_fenetre()

if __name__ == '__main__':
    main()
