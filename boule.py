from upemtk import *
from random import *
from time import *
from math import *

def fond(): 
    cree_fenetre(1280, 720)
    rectangle(-1,-1,1280,720,"darkcyan","darkcyan")
    rectangle(50,100,1280-50,720-50,"floralwhite","floralwhite")
    rectangle(1130, 680, 1230, 715, "black","red", 1, "Quitter")
    texte(1143, 685, "Quitter", "white", "nw", taille="16")

def aire_cercle(rayon):
	return pi*rayon**2

def detection_tour(tour, listeJoueur, numero_tour):
    efface("tour")
    texte(50, 50,"Tour : " + listeJoueur[tour],"lightcyan", "w",police="",tag="tour")
    texte(1280-50, 50, "Tour n° "+ str(numero_tour) + "/5", "lightcyan","e",police="",tag="tour")

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
            x, y = clic_x(ev), clic_y(ev)
            
            if 1130<=x<=1230 and 680<=y<=715:
                break

            while x<50 or x>1230 or y<100 or y>670:
                x, y, m = attente_clic()
            
            if 50<=x<100:
                x=100
            elif 1170<x<=1230:
                x=1170
            if 100<=y<150:
                y=150
            elif 620<y<=670:
                y=620
        
            intersection_cercle = 0

        
#---------Division des cercles rouges---------#

            if tour == 0:
                for i in range(len(liste_cercle_violet)):
                    distance = (x-liste_cercle_violet[i][0])**2 + (y-liste_cercle_violet[i][1])**2
                    if sqrt(distance) < liste_cercle_violet[i][2] + rayon and sqrt(distance) > liste_cercle_violet[i][2]:
                        intersection_cercle += 1
                    elif sqrt(distance) < liste_cercle_violet[i][2]:
                        scinder("red") #A modifier
                        intersection_cercle += 1
                        break
                    
#---------Division des cercles verts---------#

            if tour == 1:
                for i in range(len(liste_cercle_vert)):
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

            if numero_tour == 6 and tour == 1:
                score_vert = 0
                score_violet = 0
                for element in liste_cercle_vert:
                    score_vert += aire_cercle(element[2])
                for element in liste_cercle_violet:
                    score_violet += aire_cercle(element[2])
                if score_vert > score_violet:
                    texte(640, 50, "Le Joueur Vert gagne", "white", "center")
                elif score_violet < score_vert:
                    texte(640, 50, "Le Joueur Violet gagne", "white", "center")
                else:
                   texte(640, 50, "Egalité", "white", "center")
                break
            
            if tour == 1:
                numero_tour += 1
        
        mise_a_jour()

    ferme_fenetre()

if __name__ == '__main__':
    main()
