
def robot_planete(nb_planetes:int ,nb_robot:int , nb_tour: int) -> list :
    """ simulation de l'évolution du nombre de robot """
    res = []
    res1 = []
    x = 0  # variable temporaire qui sert à faire répeter boucle pour ajouter le nombre de robot + planete dans liste dans base 
    y = 0  # variable temporaire qui sert  à ajouter difference quand nb_robot est supérieur à nb_planete
    z = 1  # variable temporaire qui sert pour faire repeter boucle pour créer prochaine suite en foction de nb_tour
    a = 0  # variable temporaire qui sert de total de robot dans un siècle
    b = 0  # variable temporaire qui sert  à faire répeter boucle pour ajouter le nombre de robot + planete dans liste dans simulation

    if (nb_robot > 1) and (nb_robot > nb_planetes)  :
        y = nb_robot - nb_planetes
        res.append(y+1)
        y = y +1
        print(res)
        print(y)
        while ( y != nb_robot) :
            res.append(1)
            y = y +1   
            print(res)
            print(y)
    elif  (nb_robot >= 1) and (nb_robot <= nb_planetes) :
        x = y 
        while ( x != nb_robot ) :
                res.append(1)
                x = x+1
                y = y + 1
                print(res)
                print(x)
        while ( x <= y ) :
                res.append(0)
                x = x+1
                
                print(res)
                print(x) 
    elif ( x <= nb_planetes ) or (y <= nb_planetes) :
            res.append(0)
            x = x + 1
            y = +1
            print(res)
            print(x)
            print(y)
    if len(res)+1 > nb_planetes :
        res.remove( res[-1] )
    
        print(res)
        
    while ( z < nb_tour ) :
        print(z)
        a = sum(res)
        z = z+1 
        for elt in res :
            res1.append(a-elt)
        res = res1
        res1 = []
    return res 

