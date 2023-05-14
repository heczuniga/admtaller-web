
# Rutina que convierte un texto a número manejando la excepción en caso de no poder convertirlo
def convierte_entero(text) -> int:
    try:
        return int(text)
    except ValueError:
        return 0
