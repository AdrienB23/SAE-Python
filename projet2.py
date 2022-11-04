from upemtk import *
from math import *

def circle(couleur):
    global x, y, rayon, taglist_lime, taglist_red
    tag = cercle(x, y, rayon, "black", couleur, 1)
    if couleur=="lime":
        taglist_lime.append([x, y, rayon, tag])
    else:
        taglist_red.append([x, y, rayon, tag])
        
def scinder(couleur):
    global x, y, taglist_lime, taglist_red, element
    rayon1 = round(element[2]-sqrt(distance))
    tag = cercle(x, y, rayon1, "black", couleur, 1)
    if couleur=="lime":
        taglist_lime.append([x, y, rayon1, tag])
    else:
        taglist_red.append([x, y, rayon1, tag])

    if x - element[0] == 0:
        m2 = x
    else:
        m2 = (y-element[1])/(x-element[0])
    m3 = 0
    calcul = abs((m2-m3)/(1+m3*m2))
    gamma = atan(calcul) * (180/pi)
    alpha = (90-gamma) * (pi/180)
    x1 = sin(alpha)*round(element[2]-sqrt(distance))
    y1 = cos(alpha)*round(element[2]-sqrt(distance))
    if element[0]-x < 0:
        x1 = round(element[0]-x1)
    else:
        x1 = round(element[0]+x1)
    if element[1]-y < 0:
        y1 = round(element[1]-y1)
    else:
        y1 = round(element[1]+y1)


    rayon2 = round(element[2]-round(element[2]-sqrt(distance)))

    tag = cercle(x1, y1, rayon2, "black", couleur, 1)
    if couleur=="lime":
        taglist_lime.append([x1, y1, rayon2, tag])
        taglist_lime.pop(taglist_lime.index(element))
        efface(element[3])
    else:
        taglist_red.append([x1, y1, rayon2, tag])
        taglist_red.pop(taglist_red.index(element))
        efface(element[3])

if __name__ == "__main__":
    cree_fenetre(1350, 700)
#---------Initialisation des variables---------#
    taglist_lime=[]
    taglist_red=[]
    rayon = 50
    tour="lime"
    rectangle(50,100,1300,650)
    #rectangle(100,150,1250,600,)
    while True:
#---------Texte indiquant quel joueur doit jouer---------#
        if tour=="lime": 
            joueur="Tour du Joueur 1"
        else:
            joueur="Tour du Joueur 2"
        texte(550, 20, joueur, "black", "nw", "Purisa", 24, "Texte")
#---------En attente du clic de l'un des joueurs---------#
        x, y, m = attente_clic()
#---------Les joueurs ne doivent pas cliquer en dehors de la bordure---------#
        while x<50 or x>1300 or y<100 or y>650:
            x, y, m = attente_clic()
###---------Division et ajout des cercles---------###
        intersection = 0
        annulation=False
#---------Division des cercles rouges---------#
        if tour=="lime":
            for i in range(len(taglist_red)):
                element=taglist_red[i]
                distance = (x-taglist_red[i][0])**2 + (y-taglist_red[i][1])**2
                if sqrt(distance) < taglist_red[i][2]+rayon and sqrt(distance) > taglist_red[i][2]:
                    intersection += 1
                elif sqrt(distance) < taglist_red[i][2]:
                    scinder("red")
                    intersection += 1
                    break
#---------Division des cercles verts---------#
        if tour=="red":
            for i in range(len(taglist_lime)):
                element=taglist_lime[i]
                distance = (x-taglist_lime[i][0])**2 + (y-taglist_lime[i][1])**2
                if sqrt(distance) < taglist_lime[i][2]+rayon and sqrt(distance) > taglist_lime[i][2]:
                    intersection += 1
                elif sqrt(distance) < taglist_lime[i][2]:
                    scinder("lime")
                    intersection += 1
                    break
#---------Ajout des cercles---------#
        if intersection == 0:
            circle(tour)

        mise_a_jour()
#---------Changement de joueur---------#
        if tour=="lime":
            tour="red"
        else:
            tour="lime"
        
        efface("Texte")

    ferme_fenetre()
