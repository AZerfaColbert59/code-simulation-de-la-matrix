
def robot_planete(nb_planetes:int ,nb_robot:int , nb_tour: int) -> list :
    """ simulation de l'évolution du nombre de robot """
    res = [] # resulta
    res1 =[] # liste = res permetant de creer nouvelle list 
    y = 0  # variable temporaire qui sert  à creer list 
    z = 1  # variable temporaire qui sert pour faire repeter boucle pour créer prochaine suite en foction de nb_tour
    a = 0  # variable temporaire qui sert de total de robot dans un siècle

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

    while len(res) < nb_planetes:
        res.append(0)
        print(res)
        
    while ( z < nb_tour ) :
        print(z)
        a = sum(res)
        z = z+1 
        for elt in res :
            res1.append(a-elt)
        res = res1
        res1 = []
    print(sum(res))
    return res 

