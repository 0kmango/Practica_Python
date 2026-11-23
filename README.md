# Practica_Python

Ejercicios y juegos de consola en Python, hechos durante las clases.
**Todos usan solo la biblioteca estándar**: no hay que instalar dependencias.

## Requisitos

- Python **3.8 o superior** (`python --version`).
- **Windows** para `EstacionDeServicio.py` y `Maquina de bebidas.py`:
  el primero lee el PIN con `msvcrt.getch()` y el segundo limpia la pantalla
  con `os.system("cls")`, que no existen en Linux/macOS.

## Scripts

| Archivo | Qué hace | Detalle técnico |
| :--- | :--- | :--- |
| `CombinacionesPosibles.py` | Pide una palabra y muestra todas sus permutaciones | `itertools.permutations` + `set` para no repetir |
| `dislexia.py` | Cambia la primera y la última sílaba de cada palabra de una frase | separación por vocales |
| `Generador de contraseña.py` | Genera contraseñas de hasta 18 caracteres en 3 niveles | `random`, `string`, animación con `time.sleep` |
| `Maquina de bebidas.py` | Máquina expendedora con stock, precios y validación de pago | control de stock por producto |
| `EstacionDeServicio.py` | Estación de servicio con PIN de tarjeta (oculto con `*`) | `msvcrt.getch()` — **solo Windows** |
| `Gestion de contactos.py` | CRUD de contactos en memoria: agregar, buscar, editar, eliminar, listar | menú por consola |
| `JuegosFriv.py` | Minijuego «adivina el número» con intentos limitados | `random`, `sys` |

## Cómo ejecutar

```bash
python "CombinacionesPosibles.py"
```

En Windows, si tienes varias versiones de Python instaladas:

```bat
py "Maquina de bebidas.py"
```

## Notas

- Son ejercicios de práctica: la entrada es interactiva, así que no hay pruebas
  automatizadas.
- Los datos viven solo en memoria mientras el programa está abierto (no se
  guardan en disco), salvo que el propio script lo indique.