"""
Actividad relacionada con la lección 4:

    1. Haciendo uso de comprensión de listas realice un programa que, dado
    una lista de listas de números enteros, devuelva el máximo de cada
    lista. Por ejemplo, suponga la siguiente listas de listas:
    [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
    El programa debe devolver el mayor elemento de cada sublista
    (señalado en negrita).
    Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea
    donde ha implementado la compresión de listas. Haga pruebas
    mostrando el contenido de las variables y continuar con la ejecución
    línea a línea. ¿Qué conclusiones obtiene?

    2. Haga uso de la función filter para construir un programa que, dado
    una lista de n números devuelva aquellos que son primos. Por
    ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente
    debe devolver como resultado [3, 5, 5, 13]

"""


def max_sublists(sublists=None):
    n_max_list = []
    if sublists is not None:
        for sublist in sublists:
            n_max = sublist[0]
            for element in sublist:
                if element > n_max:
                    n_max = element
            n_max_list.append(n_max)
    return n_max_list


def is_prime(n, div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            return False
        else:
            return is_prime(n, div - 1)
    else:
        return 'True'


print(max_sublists([[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]))
print(list(filter(is_prime, [3, 4, 8, 5, 5, 22, 13])))
