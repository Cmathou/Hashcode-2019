tags = [ ["Coucou","Bonjour"], ["Hello", "yep"] ]

def SelectImag(identifiant) : 
    global tags
    taille = len(tags)  #nombre d'image
    maxi = 0            #score maximal
    numero = 0          #numero de l'image avec le score maximal
    idcourant = 0       #numero de l'image a traiter
    if identifiant == 0 :
        idcourant = 1
        numero = 1
        
    while idcourant <= taille : 
        #Calcul du score de l'image en cours
        score = calcul_score(tags[identifiant], tags[idcourant])
        
        #Actualisation du score
        if score > maxi : 
            maxi = score
            numero = idcourant
        
        #Changement d'image
        idcourant += 1
        
        #Cas ou on arrive sur l'image en cours
        if idcourant == identifiant :
            idcourant += 1
            
    return numero
    
    
    
