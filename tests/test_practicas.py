"""Pruebas de las funciones puras de los ejercicios.

Los scripts originales ejecutaban `input()` al importarse, así que no se podían
probar. Al mover la parte interactiva a `main()` (protegida con
`if __name__ == "__main__":`) la lógica queda importable y verificable.

Ejecución:

    pytest -q
"""

from __future__ import annotations

import pytest

from CombinacionesPosibles import genComb
from dislexia import alterar_silabas, dividir_silabas, procesar_frase


# --- CombinacionesPosibles ---

@pytest.mark.parametrize("palabra, esperado", [
    ("ab", {"ab", "ba"}),
    ("aba", {"aab", "aba", "baa"}),      # el `set` elimina las repetidas
    ("abc", {"abc", "acb", "bac", "bca", "cab", "cba"}),
    ("a", {"a"}),
])
def test_gen_comb_genera_permutaciones_unicas(palabra, esperado):
    assert genComb(palabra) == esperado


def test_gen_comb_cuenta_permutaciones_de_letras_distintas():
    assert len(genComb("abcd")) == 24       # 4!


# --- dislexia: división en sílabas ---

@pytest.mark.parametrize("palabra, esperado", [
    ("hola", ["ho", "la"]),
    ("mundo", ["mu", "ndo"]),
    ("sol", ["sol"]),
    ("computadora", ["co", "mpu", "ta", "do", "ra"]),
])
def test_dividir_silabas(palabra, esperado):
    assert dividir_silabas(palabra) == esperado


def test_dividir_silabas_no_falla_con_palabras_sin_vocales():
    """Antes lanzaba `IndexError` al no existir una sílaba previa."""
    assert dividir_silabas("xyz") == ["xyz"]


def test_dividir_silabas_con_cadena_vacia():
    assert dividir_silabas("") == []


# --- dislexia: alteración de sílabas ---

@pytest.mark.parametrize("palabra, esperado", [
    ("hola", "laho"),
    ("mundo", "ndomu"),
    ("sol", "sol"),          # una sola sílaba: no cambia
    ("", ""),
])
def test_alterar_silabas(palabra, esperado):
    assert alterar_silabas(palabra) == esperado


def test_procesar_frase_alterar_cada_palabra():
    assert procesar_frase("hola mundo") == "laho ndomu"


def test_procesar_frase_no_falla_con_palabras_sin_vocales():
    assert procesar_frase("hola xyz") == "laho xyz"