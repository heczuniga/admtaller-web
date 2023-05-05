
import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/principal/{cod_perfil}/")
@template()
def principal(cod_perfil: int):
    
    if cod_perfil == 0:
        return {
            "login": "admin",
            "autenticado": True,
            "cod_perfil": 0,
            "nom_perfil": "Administrador",
            "cod_carrera": None,
            "nom_carrera": None,
        }

    if cod_perfil == 1:
        return {
            "login": "jmoya@duoc.cl",
            "autenticado": True,
            "cod_perfil": 1,
            "nom_perfil": "Administrador de carrera",
            "cod_carrera": 1,
            "nom_carrera": "Gastronomía",
        }

    if cod_perfil == 2:
        return {
            "login": "m.gutierrez2@profesor.duoc.cl",
            "autenticado": True,
            "cod_perfil": 2,
            "nom_perfil": "Docente",
            "cod_carrera": 1,
            "nom_carrera": "Administración hotelera",
        }
