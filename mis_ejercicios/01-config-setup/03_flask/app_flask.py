# pylint: disable=missing-docstring

import os

def app_on():
    """returns the right message"""
    # $CHALLENGIFY_BEGIN
    env = os.getenv('ENV_of_FLASK_APP')
    if env:
        return f"Iniciando en modo de {env}..."
    return "Iniciando en modo vacio..."
    # $CHALLENGIFY_END

if __name__ == "__main__":
    print(app_on())
