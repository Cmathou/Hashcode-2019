def calcul_score(lst1, lst2):
    score0 = 0 #common tags
    score1 = 0 #only in 1
    score2 = 0 #only in 2
    
    tags1 = lst1[3::]
    tags2 = lst2[3::]
    
    for tag in tags1:
        if tag in tags2:
            score0 += 1
    score1 = max(len(tags1)-score0, 0)
    score2 = max(len(tags2)-score0, 0)
    
    score_final = min(score0, score1, score2)
    
    return score_final 
    
     
def SelectImag(identifiant, tags, slides) :
    taille = len(tags)  #nombre d'image
    maxi = 0            #score maximal
    numero = 0          #numero de l'image avec le score maximal
    idcourant = 0       #numero de l'image a traiter
    score = 0
    if identifiant == 0 :
        idcourant = 1
        numero = 1
    while idcourant < taille : 
        if tags[idcourant][0] in slides : 
            idcourant += 1
        else :
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
    

def CreaSlide(premiereImage, tags, slides) :
    
    imageSuivante = premiereImage
    
    while len(tags) != len(slides) :
        image = tags[imageSuivante]
        identifiant = image[0]
        slides.append(identifiant)
        imageSuivante = SelectImag(imageSuivante, tags, slides)





















