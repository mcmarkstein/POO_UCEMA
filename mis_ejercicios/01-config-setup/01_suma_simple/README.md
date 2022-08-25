Vamos a empezar con un ejemplo simple de cómo funcionan estos tipos de ejercicios.

## ¿Cuál es la metodología de resolución'

Algunos ejercicios pueden tener un  `Makefile`. que esto permite chequear si un challenge es correcto o no donde los test ya fueron elaborados por Fede y Javi. Para correr el script en la terminar tenes que usar `cd` hasta el folder y correr:

``` bash
make
```

Tu objetivo es implementar `sum4` que está en el modulo `suma_simple.py`. Los pasos son por lo general.

1. Leer las instrucciones del ejercicio.
1. Abrir el archivo,en este caso `suma_simple.py` donde tenes que escribir el código y resolverlo.
1. Correr dentro de la carpeta `make`
1. Leer los errores y ver si tienen sentido. Si no entendes el error googlealo
1. Volve a cambiar el código en  `suma_simple.py`
1. Corré de nuevo `make`
1. Nuevos errores? Estas progresando!
1. Repetí hasta que este todo correcto
1. Chequea que este correcto el score `10.00/10`
1. Commit & push tus cambios:
  1. `git status` para ver que cambios fueron hechos desde tu último commit
  1. `git diff` para ver diferencias en archivos.
  1. `git add suma_simple.py`
  1. `git commit -m "Resolví el primer erjercicio"`
  1. `git push origin master`

No tengas dudas de abriri el `Makefile` y observarlo. Por default corre  `pylint` y `pytest` chequea si está correcto y estilo. Si queres chequearlos por separado podes hacerlos así

```bash
make pylint
make pytest
```

## Recap

El objetivo era correr los test para evaluar el código y entrar en el feedback loop de trabajo.

## Para más detalles

- [pytest](https://docs.pytest.org/en/latest/)
- [pylint](https://www.pylint.org/) to enforce the [PEP 8 - Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)

(using [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)