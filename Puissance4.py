#créé par Antoine Ponthieu et Rayan Hubert.
B = [[0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0]]

joueurs = [
    [1, "", "noir", "⚫"], # caractéristiques du joueur 1
    [2, "", "blanc", "⚪"]] # caractéristiques du joueur 2

def Puissance_4():
    """ fonction de départ qui permet de lancer le jeu et qui appelle les fonctionss
    dont on a besoin.
    renvoie : pas de valeur renvoyée
    """
    definir_joueurs()
    tour_de_jeu = 0
    while not fin():
        Affichage_tableau()
        jouer(joueurs[tour_de_jeu%2]) # le %2 permet de basculer entre 0 et 1 pour indiquer pair / impaire de tour_de_jeu ce qui permet de basculer entre le joueur 1 et 2
        tour_de_jeu += 1   # passe au tour suivant (si tour pair -> joueur 1, si tour impair -> joueur 2)

def definir_joueurs():
    """ fonction qui demande aux joueurs leur nom et les stocke
    renvoie : pas de valeur renvoyéé
    """
    for j in joueurs:
        j[1]=input("Choisissez le nom du joueur " + j[2])
    for j in joueurs:
        print(j[1]," est le joueur", j[2])


#Affichage du tableau :
def Affichage_tableau():
    """Fonction d'affichage du tableau représentant le plateau de jeu
    renvoi : pas de valeur renvoyée
    """
    for i_inverse in range(len(B)):  # donne tous les indices des lignes
        i_ligne = len(B) - i_inverse - 1 #inverse le tableau pour que les pions se posent en bas
        for i_colonne in range(len(B[i_ligne])):  # donne tous les indices des colonnes dans ces lignes
            la_case = B[i_ligne][i_colonne]
            if la_case==0:
                print("  ",end=" | ")
            elif la_case==1:
                print(joueurs[la_case - 1][3],end=" | ") # affiche le jeton du joueur "la_case" qui se trouve à l'indice la_case- 1 du tableau joueurs
            else:
                print(joueurs[la_case - 1][3],end=" | ") #affiche le jeton du joueur "la_case" qui se trouve à l'indice la_case- 1 du tableau joueurs
        print()  # retour à la ligne
    for i in range(len(B[0])):
        print(i + 1,  end="    ")
    print()

def jouer(joueur):
    """fonction qui permet a chaque joueur d'entrer la colonne a laquelle ils
    souhaitent jouer et qui vérifie que la colonne est jouable
    joueur : list
    renvoi : aucune valeur renvoyée
    """
    reponse = input(joueur[1] + ", choisissez où vous voulez jouer")
    jeton_c = -1  #reponse invalide
    if reponse.isdigit():  #verifie qu'il n'y a que des chiffres
        jeton_c = int(reponse) - 1  #enlève 1 pour avoir l'indice
    if jeton_c < 0 or jeton_c > len(B[0]) :
        print("Choix de colonne invalide, veuillez réessayer.")
        return jouer(joueur)  # si indice invalide, on rappelle la fonction ce qui demande de rejouer
    ligne = 0  # on part de la supposition qu'on joue à la première ligne
    while ligne < len(B) and B[ligne][jeton_c] != 0   :  #cherche la première ligne disponible tout en testant au préalable qu'on ne dépasse le nombre de lignes maximum
        ligne += 1
    if ligne >= len(B):  #verifie si la colonne est pleine
        print("cette colonne est pleine, veillez jouer autre part")
        return jouer(joueur)  # si colonne pleine, on rappelle la fonction ce qui demande de rejouer
    B[ligne][jeton_c] = joueur[0]

# Fonction importante a mettre dans le diapo
def verif_direction(num_joueur, x, y, dx, dy, score):
    """fonction qui vérifie dans une direction donnée si 4 jetons identiques
    sont alignés
    num_joueur : int
    x : int
    y : int
    dx : int
    dy : int
    score : int
    """
    if x < 0 or y < 0 or x >= len(B[0]) or y >= len(B): #verifie si on est en dehors des limites du tableau
        return False  # sortie des limites sans avoir 4 donc jamais 4 dans cette direction
    if B[y][x] == num_joueur:  #verifie si le numéro du joueur est égal au numéro de la case
        score = score + 1  #augmente le score de 1 si le numéro du joueur est égal au numéro de la case
    else :
        return False  # si num_joueur est différent du numéro stocké dans la case (B[y][x]) alors pas 4 jetons d'affilés
    if score == 4:
        return True  #si le score est égal à 4 alors renvoie True pour dire que le joueur en question gagne
    return verif_direction(num_joueur, x + dx, y + dy, dx, dy, score) # on ajoute la distance dx à x et la distance dy à y pour sauter à la prochaine case toujours dans la même direction (dx, dy)

def verif_si_vainqueur():
    """fonction qui vérifie si il existe un vaincqueur
    renvoi : int
    """
    directions = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)) #définit toutes les directions sous forme de vecteurs
    for y in range(len(B)):  # pour toutes les lignes
        ligne_est_vide = True  # variable qui suppose que la ligne est vide
        for x in range(len(B[y])):  # pour toutes les colonnes de la ligne
            if B[y][x] != 0 :  # si le numéro contenu dans la case est différent de 0
                ligne_est_vide = False  # la ligne n'est pas vide, il y a au moins 1 joueur qui y a jouer
                for d in directions:  # pour les 8 directions possibles
                    if verif_direction(B[y][x], x, y, d[0], d[1], 0) == True: # verifier si dans une direction on a 4 jetons identiques alignés
                        return B[y][x]  # numéro du joueur qui a gagné
        if ligne_est_vide == True:
            return 0  # aucun joueur n'a gagné
    return 0 # aucun joueur n'a gagné



def tableau_plein():
    """fonction qui vérifie si le tableau est plein, c'est à dire si toutes les
    positions sont jouées
    renvoi : bool
    """
    for i_ligne in range(len(B)):  # pour toutes les lignes
        for i_colonne in range(len(B[i_ligne])):  # pour toutes les colonnes
            if B[i_ligne][i_colonne] == 0:  # verifie si il rester une case libre dans le tableau
                return False  # le jeu peut continuer
    return True  # le tableau est plein le jeu doit s'arrêter


def fin():
    """fonction qui détermine si la partie est terminée soit quand un joueur
    gagne soit quand le plateau est plein
    renvoi : bool
    """
    resultat = verif_si_vainqueur()  # on récupère le numéro du vaincqueur ou 0
    if resultat != 0:
        Affichage_tableau()
        print(joueurs[resultat - 1][1], "a gagné !")  # le joueur à l'indice resultat - 1 a gagné
        return True
    elif tableau_plein() == True :
        Affichage_tableau()
        print("La partie est terminée, match nul !")  # si le tableau est plein
        return True
    else :
        return False  # continuer à jouer

Puissance_4()

"""Le programme est fonctionnel et le jeu est jouable. Ce que nous voyons à
améliorer a ce niveau là ce sont en premier lieu la vérification des cases que
nous faisons actuellement en 8 étapes par case que nous pouvons optimiser en
seulement 3 étapes par case et en second lieu le tableau qui est affiché
"a l'envers" car les jetons se posent en haut. Nous allons donc faire en sorte
de le retourner.
"""