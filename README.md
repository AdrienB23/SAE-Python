Variante : 
Nous avons choisi d'implémenter la variante "Sablier" à notre programme puisqu'elle est la plus accessible pour nous, comme nous n'avions jamais, ou presque, fais de python précédemment. De plus c'est une option que l'on voit assez souvent dans les jeux de stratégies, comme aux échecs, et qui permet d'imposer un temps limiter évitant que la partie s'éternise. Mais cela ne nous a pas empêché de rencontrer quelques problèmes que nous avions pu régler plus ou moins rapidement. Notamment lorsqu'on voulait faire le sablier, on est parti d'une fonction qui faisait un compte-à-rebours, or le problème était qu'on ne pouvait pas cliquer lorsque celui-ci s'activait. On a alors complètement changé la fonction puisqu'ne trouvait pas d'autres solutions alternatives, et on l'a défini autrement, ce qui a pris encore plus de temps.

Organisation du programme :
Le programme a été créé de façon progressive, c'est-à-dire qu'au fur et à mesure nous avons rajouté les différentes fonctions nécessaires à la création du jeu mais nous n'avons pas réellement eu un ordre de priorité lors de son élaboration. Nous avons regroupé par thèmes nos différentes fonctions pour une meilleure lisibilité. Les fonctions ont été pensé pour essayer d'atteindre la plus petite complexité à cause du programme qui est tout de même assez lourd mais fonctionnel.  
Nous n'avons pas tout mis dans des fonctions comme par exemples, les différentes variables qui sont initialiser au début d'une boucle. Nous avons pris le choix d'utiliser une boucle while true car il est plus simple pour nous de gérer les tours des joueurs grâces a un modulo

Explication de la fonction scinder():
Cette fonction consiste en un calcul dans un premier temps, des rayons des deux différents petits cercle, ensuite la fonction calcul l'équation de deux droites : 
- la droite (1) passant par le centre du grand cercle initial et du centre du nouveau petit cercle grâce aux cordonnées du clic du joueur
- la droite (2) vertical passant par le centre du nouveau petit cercle grâce aux cordonnées du clic du joueur

Ensuite, un calcul d'angle est nécessaire car on doit connaître les cordonnées x et y de l'intersection entre la droite (1) et le contour du cercle
Formule utilisé pour le calcul de l'angle : tan(alpha) = abs( (m2-m1)/(1+m1\*m2) )
Grâce à l'angle, nous pouvons utiliser la trigonometrie pour connaitre la longueur C et la longueur B pour retrouver le point d'intersection voulu,
et donc nous pouvons déterminer le centre du second cercle en répétant ces déplacements a partir du centre du grand cercle initial.

   /|<---- Angle alpha
A / |C
 /__|
