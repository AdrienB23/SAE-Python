from upemtk import *
from math import *

def circle(couleur):
    global x, y, rayon, taglist
    tag = cercle(x, y, rayon, "gray", couleur, 1)
    taglist.append([x, y, rayon, tag])

def scinder(couleur):
    global x, y, taglist, element
    rayon1 = round(element[2]-sqrt(distance))
    tag = cercle(x, y, rayon1, "black", couleur, 1)
    taglist.append([x, y, rayon1, tag])

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
    taglist.append([x1, y1, rayon2, tag])

    taglist.pop(taglist.index(element))
    efface(element[3])

if __name__ == "__main__":
    taglist=[]
    cree_fenetre(1350, 700)
    rayon = 50
    tour="lime"
    rectangle(50,100,1300,650)
    marque(50,100)
    marque(50, 650)
    marque(1300,100)
    marque(1300,650)
    while True:
        if tour=="lime":
            joueur="Tour du Joueur 1"
        else:
            joueur="Tour du Joueur 2"
        texte(475, 50, joueur, "black", "nw", "Purisa", 24, "Joueur")
        
        x, y, m = attente_clic()
        
        intersection = 0
        for element in taglist: # Division des cercles
            distance = (x-element[0])**2 + (y-element[1])**2
            if sqrt(distance) < element[2]+rayon and sqrt(distance) > element[2]:
                intersection += 1
            elif sqrt(distance) < element[2]:
                if tour=="lime":
                    scinder("red")
                else:
                    scinder("lime")
                intersection += 1
                break
        
        if intersection == 0 and 50<=x<=1300 and 100<=y<=650 :
            circle(tour)
        mise_a_jour()
        
        if tour=="lime":
            tour="red"
        else:
            tour="lime"
        
        efface("Joueur")
    
    ferme_fenetre()
