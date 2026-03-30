from random import randint
def robot_planete(nb_planetes: int, nb_robots_initiaux: int, nb_siecles: int) -> list:
    """
    Simule la répartition des robots sur chaque planète de la galaxie au fil des siècles.        list: Une liste représentant le nombre de robots sur chaque planète après `nb_siecles`.
    """
    # Répartition initiale des robots
    galaxie = []
    robots_restants = nb_robots_initiaux

    # Répartit les robots en surplus
    if nb_robots_initiaux > nb_planetes:
        robots_restants = nb_robots_initiaux - nb_planetes
        galaxie.append(robots_restants + 1)
        robots_restants += 1

    # Ajouter un robot sur chaque planète restante
    while robots_restants < nb_robots_initiaux:
        galaxie.append(1)
        robots_restants += 1

    while len(galaxie) < nb_planetes:
        galaxie.append(0)

    # Simulation sur plusieurs siècles
    for siecle in range(1, nb_siecles):
        total_robots = sum(galaxie)

        # Chaque robot envoie une réplique vers chaque planète puis s'autodétruit
        galaxie = [total_robots - robots for robots in galaxie]

    return galaxie

def type_suite(nb_planete: int, nb_robot: int) -> str:
    nb_tour2 = 0
    for nb_tour2 in range(1, 11):
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
            print(res[-3:])
    return res