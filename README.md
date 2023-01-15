Dans ce troisième et dernier rendu, nous avons implanté les différents bonus requis tel que la configuration du jeu, la classement, la pause/sauvegarde et la configuration des obstacles.

Pour réaliser la configuration du jeu, nous avons initiallement ajouté un fichier " configuration.txt " pour ensuite intégrer les différentes options modifiable comme la couleur des différentes boules ou encore les touches du clavier pour les différents bonus/variante, cependant nous avons eu du mal a ajouté la taille de la fenêtre et la talle du terrain de jeu, nous avons donc décider de malgré tout implanté ce bonus sans nécessaire avoir comme possibilité de modifier ces deux paramètres. Nous voulons que notre jeu respecte une certaine taille, c'est un choix arbitraire mais cela nous simplifera bien des choses. Nous n'avous pas eu de réel problème a part bien séparer les différentes lignes du fichier et en supprimant les saut de ligne a la fin de chaque ligne.

Ensuite, le bonus classement, nous avons tout d'abord chercher à comment récuperer les informations des différentes touches du clavier pour ensuite les afficher a l'écran. Nous avons aussi rencontrer quelque difficulté, notamment pour faire en sorte de trier le classement de manière décroissante afin d'afficher le meilleur score en haut de la liste, il fallait aussi actualiser le fichier. De plus, ayant voulu ajouter une certaine limite, nous devions remplacer le score le plus bas par le nouveau score s'il est supérieur pour éviter qu'il y ai un encombrement dans le tableau des scores.

Enfin, pour le bonus obstacles, nous avons décider d'utiliser un certain encodage de cette forme : %x;%y;r;couleur 
avec : %x = Pourcentage de la largeur de l'aire de jeu, si à 0% = Gauche, si 100% = Droite
De même pour %y = Pourcentage de la hauteur de l'aire de jeu, si à 0% = Haut, si 100% = Bas
r = Rayon des différents obstacles
couleur = Couleur des différents obstacle
Ce bonus est aussi l'une des raisons du pourquoi nous avons décider de ne pas intégrer la taille de la fene^tre et de l'aire de jeu car il fallait adapté les positions des obstacles en fonction de la taille.
Nous avons eu quelques soucis car il fallait trouver les bonnes formules pour les bonnes positions des obstacles, et faire en sorte qu'ils ne dépassent pas du cadre

Informations supplémentaire : 
Classement : Nous avons décider de garder un historique de tout les scores, malgré qu'il y ai plusieurs fois un même nom, cela peut être intéressant pour comparer ses différents score des différentes parties.
Malgré les problèmes concernants l'adaptation du jeu en fonction de la taille de fenêtre/aire de jeu, nous avons pris cette décision car nous avons eu trop tard l'idée de rajouter une première fenêtre pour permettre à l'utilisateur de choisir différentes taille normalisé ( 1920x1080, 1280x720, 640x480 etc... ) Pour ainsi adapté la fenêtre au choix de l'utilisateur.

Problèmes majeurs rencontré : 
Nous avons tenté de réaliser les deux bonus Billard et Pause/Sauvegarde, cependant lors de la réalisation de ceux-ci, nous avons remarqué que la structure de notre prograrmme n'étais pas réellement adapté a ces bonus, plus particulièrement Pause/Sauvegarde, de plus, nous avons eu eu du mal a gérer toutes les informations nécessaire à une sauvegarde, certaiesn ambiguité et conflit entre plusieurs parties du programme posait problème pour tout le reste. Pour le cas du bonus Billard, nous n'avons pas réussi à bien comprendre les différentes subtilité, tel que la collision entre deux boules, car effectivement, nous avons trouver qu'il y a un certain sens dans leur collision grâce à la tangente, cependant, dans le billard que tout le monde connait, lorqsu'il y a collision entre deux boules, l'une bouge et non l'autre, or dans notre cas les boules bougent sans arrêt.

- Baffioni Adrien
- Cherak Rabah
Université Gustave Eiffel - Projet Python Bataille de Boule
