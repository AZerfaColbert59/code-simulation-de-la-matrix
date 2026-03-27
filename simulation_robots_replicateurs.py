from random import randint
def robot_planete(nb_planetes:int ,nb_robot:int , nb_tour: int) -> list :
    """ simulation de l'évolution du nombre de robot """
    res = [] # resulta
    res1 =[] # liste = res permetant de creer nouvelle list 
    surplus = 0  # variable temporaire qui sert  à creer list 
    loop_tour = 1  # variable temporaire qui sert pour faire repeter boucle pour créer prochaine suite en foction de nb_tour
    sum_robot = 0  # variable temporaire qui sert de total de robot dans un siècle

    if (nb_robot > 1) and (nb_robot > nb_planetes)  :
        surplus = nb_robot - nb_planetes
        res.append(surplus+1)
        surplus = surplus +1
        #print(res)
        #print(surplus)
    while ( surplus != nb_robot) :
            res.append(1)
            surplus = surplus +1   
            #print(res)
            #print(surplus)

    while len(res) < nb_planetes:
        res.append(0)
        #print(res)
        
    while ( loop_tour < nb_tour ) :
        #print(loop_tour)
        sum_robot = sum(res)
        loop_tour = loop_tour+1 
        for elt in res :
            res1.append(sum_robot-elt)
        res = res1
        res1 = []
    #print(sum(res))
    return res 

def type_suite(nb_planete:int,nb_robot:int) -> str :
    nb_tour2  = 0
    while nb_tour2 <= 10:
        nb_tour2 = nb_tour2+1
        if sum(robot_planete(nb_planete,nb_robot,nb_tour2))== sum(robot_planete(nb_planete,nb_robot,nb_tour2-1)*(nb_planete-1)) :
            res = "suite géometrique"
        elif sum(robot_planete(nb_planete,nb_robot,nb_tour2))== sum(robot_planete(nb_planete,nb_robot,nb_tour2-1)) + sum(robot_planete(nb_planete,nb_robot,nb_tour2-2)) :
            res= " suite de fibonacci"
        elif sum(robot_planete(nb_planete,nb_robot,nb_tour2))== sum(robot_planete(nb_planete,nb_robot,nb_tour2-1)):
            res = "suite constante"
        else :
            res = "suite à rechercher"
        
    return  res

def boucle_test(nb_tour) :
    res = []
    x = 0
    y = 0
    a = 0
    while a != nb_tour :
        x = randint(0,100)
        y = randint(0,100)
        a = a +1
        if type_suite(x,y)== "suite à rechercher" :
            res.append(x)
            res.append(y)
            res.append("suite à rechercher")
            print(res)
        if type_suite(x,y)== "suite géometrique" :
            res.append(x)
            res.append(y)
            res.append("suite géometrique")
            print(res)
        if type_suite(x,y)== "suite de fibonacci" :
            res.append(x)
            res.append(y)
            res.append("suite de fibonacci")
            print(res)
        if type_suite(x,y)== "suite constante" :
            res.append(x)
            res.append(y)
            res.append("suite constante")
            print(res)
    return  res 
            
