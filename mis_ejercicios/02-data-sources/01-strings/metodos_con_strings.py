# pylint: disable=missing-docstring

def es_una_pregunta(a_string):
    """
    returns True if a_string termina con "?"
    example: is_a_question("Cómo andas?") => True
    """
    # $CHALLENGIFY_BEGIN
    return a_string.endswith('?')
    # $CHALLENGIFY_END

def pertence_a(a_string, a_word):
    """
    retorna True si a_word esta en a_string
    ejemplo: ("hey jude", "jude") => True
    """
    # $CHALLENGIFY_BEGIN
    return a_word in a_string
    # $CHALLENGIFY_END

def agregar_coma(a_string):
    """
    retorna una copia del string con una coma al final
    """
    # $CHALLENGIFY_BEGIN
    return ', '.join(a_string.split()) # or a_string.replace(' ', ', ')
    # $CHALLENGIFY_END


def cuenta_repetido(a_string, a_substring):
    """
    returns cuantas veces a_substring ocurre en a_string
    ejemplo: cuenta_repetido("000123000123", "0") => 6
    """
    # $CHALLENGIFY_BEGIN
    return a_string.count(a_substring)
    # $CHALLENGIFY_END



def eliminar_espacios_exteriores(a_string):
    """
    retorna una copia del string sin espacios exteriores
    ejemplo: eliminar_espacios_exteriores("  hey yo  ") => "hey yo"
    """
    # $CHALLENGIFY_BEGIN
    return a_string.strip()
    # $CHALLENGIFY_END

def reemplazar_una_letra(initial_string, old_letter, new_letter):
    """
    retorna una copia del string con la letra old_letter reemplazada por new_letter
    ejemplo: replace("argentina", "a", "o") => "argentino"
    """
    # $CHALLENGIFY_BEGIN
    return initial_string.replace(old_letter, new_letter)
    # $CHALLENGIFY_END


def f_string_nombreyapellido(nombre, apellido, edad):
    """
    retorna una frase con el nombre y apellido mayúsuclas y la edad
    ejemplo: f_string_nombreyapellido("fede", "moreno", 33) => "Fede Moreno tiene 33"
    """
    # $CHALLENGIFY_BEGIN
    return f"{nombre.capitalize()} {apellido.capitalize()} tiene {edad}"
    # $CHALLENGIFY_END
