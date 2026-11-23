"""Genera todas las permutaciones (sin repetir) de una palabra."""

from itertools import permutations


def genComb(palabra):
    """Devuelve el conjunto de permutaciones unicas de ``palabra``.

    >>> sorted(genComb("ab"))
    ['ab', 'ba']
    >>> len(genComb("aba"))
    3
    """
    combinaciones = permutations(palabra)
    return set(''.join(combinacion) for combinacion in combinaciones)


def main():
    palabra = input("\nIngrese una palabra: ")
    print(f"\nLa palabra ingresada tiene {len(palabra)} caracteres.")
    combinaciones = genComb(palabra)

    print(f"\nTodas las combinaciones posibles de '{palabra}' son {len(combinaciones)}\n")

    combinaciones = list(combinaciones)
    columnas = 6

    for i in range(0, len(combinaciones), columnas):
        fila = combinaciones[i:i + columnas - 2]
        print(' | '.join(fila))


if __name__ == "__main__":
    main()
