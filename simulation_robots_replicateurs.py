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

def type_suite(nb_planete: int, nb_robot: int) -> str:
    nb_tour2 = 0
    while nb_tour2 <= 10:
        nb_tour2 += 1
        current_sum = sum(robot_planete(nb_planete, nb_robot, nb_tour2))
        prev_sum = sum(robot_planete(nb_planete, nb_robot, nb_tour2-1))
        prev_prev_sum = sum(robot_planete(nb_planete, nb_robot, nb_tour2-2))

        if current_sum == prev_sum * (nb_planete - 1):
            return "suite géometrique"
        elif current_sum == prev_sum + prev_prev_sum:
            return "suite de fibonacci"
        elif current_sum == prev_sum:
            return "suite constante"
    return "suite à rechercher"

def boucle_test(nb_tour) :
    res = []
    x = 0
    y = 0
    a = 0
    actions = {
        "suite à rechercher": lambda: res.extend([x, y, "suite à rechercher"]),
        "suite géometrique": lambda: res.extend([x, y, "suite géometrique"]),
        "suite de fibonacci": lambda: res.extend([x, y, "suite de fibonacci"]),
        "suite constante": lambda: res.extend([x, y, "suite constante"])
    }
    while a != nb_tour:
        x = randint(0, 100)
        y = randint(0, 100)
        a += 1
        suite_type = type_suite(x, y)
        if suite_type in actions:
            actions[suite_type]()
            print(res[-3:])  # Affiche uniquement les trois derniers éléments ajoutés
    return res