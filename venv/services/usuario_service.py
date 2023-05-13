
from typing import Optional
from data.usuario import Usuario
from data.perfil import Perfil


def get_id_usuario_by_login(login: str) -> Optional[int]:
    if login == "admin@duoc.cl":
        return 1

    if login == "jmoya@duoc.cl":
        return 2

    if login == "maalvarez@duoc.cl":
        return 3

def autenticacion(login: str, password: str) -> Optional[Usuario]:
    if login == "admin@duoc.cl" and password == "admin":
        return Usuario(1, "admin@duoc.cl", "admin", "Adminstrador", "sistema", "", "")

    if login == "jmoya@duoc.cl" and password == "jmoya":
        return Usuario(2, "jmoya@duoc.cl", "jmoya", "Moya", "Plaza", "Jéssica", "Jéssica")

    if login == "maalvarez@duoc.cl" and password == "maalvarez":
        return Usuario(3, "maalvarez@duoc.cl", "maalvarez", "Álvarez", "Peña", "Marco", "Marco")

    return None


def get_perfil(id_usuario: int) -> Optional[Perfil]:
    if id_usuario == 1:
        return Perfil(0, "Administrador TI", "Administrador desde el punto de vista TI del sistema. En resumen, tiene acceso a todo. Es el alfa y el omega del sistema.")

    if id_usuario == 2:
        return Perfil(1, "Administrador de carrera", "Administrador de entidades del sistema, usuarios y perfiles. También accede a reportes de gestión.")

    if id_usuario == 3:
        return Perfil(2, "Docente", "Docentes de la carrera responsables de la ejecución del taller.")

    return None


def get_ano_academ(id_usuario: int) -> Optional[int]:
    return 2023


def get_nom_carrera(id_usuario: int) -> Optional[str]:
    if id_usuario == 1:
        return "(sin carrera)"

    if id_usuario == 2:
        return "Gastronomía"

    if id_usuario == 3:
        return "Gastronomía"

    return None
