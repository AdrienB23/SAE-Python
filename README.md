Dans ce troisième et dernier rendu, nous avons implanté les différents bonus requis tel que la configuration du jeu, le classement, la pause/sauvegarde et la configuration des obstacles.

Pour réaliser la configuration du jeu, nous avons initiallement ajouté un fichier " configuration.txt " pour ensuite intégrer les différentes options modifiable comme la couleur des différentes boules ou encore les touches du clavier pour les différents bonus/variante, cependant nous avons eu du mal a ajouté la taille de la fenêtre et la talle du terrain de jeu, nous avons donc décider malgré tout d'implanter ce bonus sans nécessairement avoir la possibilité de modifier ces deux paramètres. Nous voulons que notre jeu respecte une certaine taille, c'est un choix arbitraire mais cela nous simplifera bien des choses. Nous n'avous pas eu de réel problème a part bien séparer les différentes lignes du fichier et en supprimant les saut de ligne a la fin de chaque ligne.

Ensuite, pour le bonus classement, nous avons tout d'abord chercher à savoir comment récuperer les informations des différentes touches du clavier pour ensuite les afficher à l'écran. Nous avons aussi rencontré quelques difficultés, notamment pour faire en sorte de trier le classement de manière décroissante afin d'afficher le meilleur score en haut de la liste tout en actualisant le fichier. De plus, ayant voulu ajouter une certaine limite, nous devions remplacer le score le plus bas par le nouveau score, s'il est supérieur, pour éviter qu'il y ait un encombrement dans le tableau des scores.

Enfin, pour le bonus obstacles, nous avons décider d'utiliser un certain encodage de cette forme : %x;%y;r;couleur 
avec : %x = Pourcentage de la largeur de l'aire de jeu, où 0% = Gauche et 100% = Droite
De même pour %y = Pourcentage de la hauteur de l'aire de jeu, où 0% = Haut et 100% = Bas
r = Rayon des différents obstacles
couleur = Couleur des différents obstacle
Ce bonus est aussi l'une des raisons du pourquoi nous avons décider de ne pas intégrer la taille de la fenêtre et de l'aire de jeu car il fallait adapté les positions des obstacles en fonction de la taille.
Nous avons eu quelques soucis car il fallait trouver les bonnes formules pour les bonnes positions des obstacles, et faire en sorte qu'ils ne dépassent pas du cadre

Informations supplémentaire : 
Classement : Nous avons décidé de garder l'historique de tous les scores, malgré qu'il y ait plusieurs fois un même nom, cela peut être intéressant pour comparer ses différents scores des différentes parties.
Malgré les problèmes concernant l'adaptation du jeu en fonction de la taille de la fenêtre/aire de jeu, nous avons pris cette décision car nous avons eu l'idée trop tard de rajouter une première fenêtre pour permettre à l'utilisateur de choisir différentes tailles normalisées ( 1920x1080, 1280x720, 640x480 etc... ). Pour ainsi adapté la fenêtre au choix de l'utilisateur.

Problèmes majeurs rencontré : 
Nous avons tenté de réaliser les deux bonus Billard et Pause/Sauvegarde, cependant lors de la réalisation de ceux-ci, nous avons remarqué que la structure de notre programme n'était pas réellement adaptée à ces bonus, plus particulièrement Pause/Sauvegarde. De plus, nous avons eu du mal à gérer toutes les informations nécessaires à une sauvegarde, certaines ambiguités et conflits entre plusieurs parties du programme posaient problème pour tout le reste. Pour le cas du bonus Billard, nous n'avons pas réussi à bien comprendre les différentes subtilités, tels que la collision entre deux boules, en effet, nous avons trouvé qu'il y a un certain sens dans leur collision grâce à la tangente. Cependant, dans le billard que tout le monde connait, lorsqu'il y a une collision entre deux boules, l'une bouge et non l'autre, or dans notre cas, toutes les boules bougent sans arrêt.

- Baffioni Adrien
- Cherak Rabah
- Université Gustave Eiffel - Projet Python Bataille de Boule
