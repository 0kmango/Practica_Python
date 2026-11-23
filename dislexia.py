"""Altera las palabras de una frase cambiando su primera y ultima silaba."""

VOCALES = "aeiouáéíóúü"


def dividir_silabas(palabra):
    """Divide ``palabra`` en silabas siguiendo la regla vocal-final.

    >>> dividir_silabas("hola")
    ['ho', 'la']
    """
    silabas = []
    silaba = ""

    for letra in palabra:
        silaba += letra
        if letra.lower() in VOCALES:
            silabas.append(silaba)
            silaba = ""

    if silaba:
        # Si la palabra no tiene vocales, ``silabas`` esta vacia y no hay
        # silaba anterior a la que pegarle las consonantes finales.
        if silabas:
            silabas[-1] += silaba
        else:
            silabas.append(silaba)

    return silabas


def alterar_silabas(palabra):
    """Intercambia la primera y la ultima silaba de ``palabra``."""
    silabas = dividir_silabas(palabra)
    if len(silabas) > 1:
        silabas[0], silabas[-1] = silabas[-1], silabas[0]
    return "".join(silabas)


def procesar_frase(frase):
    """Aplica :func:`alterar_silabas` a cada palabra de la frase."""
    palabras = frase.split()
    nuevas_palabras = [alterar_silabas(palabra) for palabra in palabras]
    return " ".join(nuevas_palabras)


def main():
    frase = input("Di una frase: ")
    frase_alterada = procesar_frase(frase)
    print("\nFrase alterada:")
    print(frase_alterada)


if __name__ == "__main__":
    main()
