
import hashlib
from typing import Optional
from starlette.requests import Request
from starlette.responses import Response

from infrastructure.num_conversion import convierte_entero

# Nombre de la cookie a ser usada
autoriz_cookie: str = "cookie_admtaller"


# Setea la cookie del autorización al sistema
def set_autoriz_cookie(response: Response, id_usuario: int, login: str, cod_perfil: int, ano_academ: int, nom_carrera: str):
    hash_valor: str = __hash_text(str(id_usuario))
    valor: str = "{}:{}:{}:{}:{}:{}".format(id_usuario, login, hash_valor, cod_perfil, ano_academ, nom_carrera)
    response.set_cookie(autoriz_cookie, valor, secure=False, httponly=True, samesite="Lax")


# Retorna un texto "enciptado" que se usa para almacenar la password en la cookie y que no sea visible
def __hash_text(text: str) -> str:
    text: str = "entropia__" + text + "__universal"
    return hashlib.sha512(text.encode("utf-8")).hexdigest()


# Retorna el id del usuario conectado desde la cookie
def get_id_usuario_cookie(request: Request) -> Optional[int]:
    if autoriz_cookie not in request.cookies:
        return None

    val = request.cookies[autoriz_cookie]
    parts = val.split(":")
    if len(parts) != 6:
        return None

    id_usuario: str = parts[0]
    login: str = parts[1]
    hash_valor: str = parts[2]
    hash_val_chequear: str = __hash_text(str(id_usuario))
    if hash_valor != hash_val_chequear:
        print("Error: El hash no corresponde. Valor inválido de la cookie")
        return None

    convierte_entero(id_usuario)

    if not id_usuario:
        return None
    
    return int(id_usuario)


# Retorna el login del usuario conectado desde la cookie
def get_login_cookie(request: Request) -> Optional[str]:
    if autoriz_cookie not in request.cookies:
        return None

    val = request.cookies[autoriz_cookie]
    parts = val.split(":")
    if len(parts) != 6:
        return None

    id_usuario: str = parts[0]
    login: str = parts[1]

    if not login:
        return None

    return login


# Retorna el código del perfil del usuario conectado desde la cookie
def get_cod_perfil_cookie(request: Request) -> Optional[int]:
    if autoriz_cookie not in request.cookies:
        return None

    val = request.cookies[autoriz_cookie]
    parts = val.split(":")
    if len(parts) != 6:
        return None

    id_usuario: str = parts[0]
    login: str = parts[1]
    hash_valor: str = parts[2]
    cod_perfil: str = parts[3]

    convierte_entero(cod_perfil)

    if not cod_perfil:
        return None

    return int(cod_perfil)


# Retorna el año académico vigente del usuario conectado desde la cookie
def get_ano_academ_cookie(request: Request) -> Optional[int]:
    if autoriz_cookie not in request.cookies:
        return None

    val = request.cookies[autoriz_cookie]
    parts = val.split(":")
    if len(parts) != 6:
        return None

    id_usuario: str = parts[0]
    login: str = parts[1]
    hash_valor: str = parts[2]
    cod_perfil: str = parts[3]
    ano_academ: str = parts[4]

    convierte_entero(ano_academ)

    if not ano_academ:
        return None

    return int(ano_academ)


# Retorna el nombre de la carrera del usuario conectado desde la cookie
def get_nom_carrera_cookie(request: Request) -> Optional[str]:
    if autoriz_cookie not in request.cookies:
        return None

    val = request.cookies[autoriz_cookie]
    parts = val.split(":")
    if len(parts) != 6:
        return None

    id_usuario: str = parts[0]
    login: str = parts[1]
    hash_valor: str = parts[2]
    cod_perfil: str = parts[3]
    ano_academ: str = parts[4]
    nom_carrera: str = parts[5]

    if nom_carrera == "(sin carrera)":
        return ""

    return nom_carrera


# Elimina a cookie. Se usa en el logout del sistema
def logout(response: Response) -> None:
    response.delete_cookie(autoriz_cookie)
