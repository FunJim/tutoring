from hanoi_vision import*

Tour = [[3,2,1],[],[]]
v=Visualisation_hanoi(Tour)

def bouge(x,y):
    if len(Tour[x]) == 0:
        print("La tour de départ est vide")
    elif len(Tour[y]) == 0:
        pion = Tour[x][-1]
        Tour[x].remove(pion)
        Tour[y].append(pion)
    else:
        pion = Tour[x][-1]
        if Tour[y][-1] > pion:
            Tour[y].append(pion)
            Tour[x].remove(pion)
        else:
            print("pion pas accepte")
##bouge(0,2)
print(Tour)


def deplace2pions(depart,arrive,intermediaire):
    bouge(depart,intermediaire)
    bouge(depart,arrive)
    bouge(intermediaire,arrive)


deplace2pions(0,2,1)


v.mise_a_jour(Tour)
