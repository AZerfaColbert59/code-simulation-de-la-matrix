# code-simulation-de-la-matrix
Ce projet s’inscrit dans le cadre de l'atelier **Maths en Jeans** et simule à l'aide d'un programme Python le problème suivant.

## Problème étudié

Le Programme Python simule l'évolution du nombre de robots sur différentes planètes d'une galaxie : À chaque siècle, chaque robot envoie une réplique de lui-même vers chaque planète accessible depuis sa planète actuelle, puis s'autodétruit.

La galaxie peut être modélisée par un **graphe** :
- chaque **sommet** représente une planète ;
- une **arête** signifie qu’un robot peut voyager d’une planète à l’autre.

À chaque siècle :
- chaque robot présent sur une planète produit **un robot pour chaque planète accessible** ;
- les nouveaux robots sont envoyés vers ces planètes ;
- le robot initial **s’autodétruit**.

On cherche à comprendre **l’évolution du nombre de robots sur chaque planète au fil des siècles**, selon différentes configurations de graphes et de conditions initiales.

## Objectifs

- **Modéliser** la propagation des robots entre les planètes.
- **Simuler** l'évolution du nombre de robots sur chaque planète au fil des siècles.
- **Observer** les résultats selon les cofigurations, comme la suite de Fibonacci dans le cas de 3 planètes.
- **Permettre** une configuration flexible du nombre de planètes et de leurs connexions.

## Ressources et Liens
- [Maths en Jeans](https://www.mathsenjeans.fr)