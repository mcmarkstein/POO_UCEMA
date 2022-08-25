Una manera de modificar los scripts de Python es usando variables de enviroment

## Ejercicio 3

Abrir `app_flask.py` e implementar la función `app_on`. Debería retornar una `String` dependiendo de la variable de entorno `ENV_of_FLASK_APP`.


```bash
FLASK_ENV=desarrollo python app_flask.py
# => "Iniciando en modo de desarrollo..."

FLASK_ENV=produccion python app_flask.py
# => "Iniciando en modo de produccion..."

python app_flask.py
# => "Iniciando en modo vacio..."
```

💡 **Tip**: Leer sobre `os.getenv` en [`os`](https://docs.python.org/3/library/os.html)
