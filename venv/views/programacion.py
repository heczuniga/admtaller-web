
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
from starlette import status
from services import programacion_service

from viewmodels.programacion.programaciones_asignatura_viewmodel import ProgramacionesAsignaturaViewModel

router = fastapi.APIRouter()


@router.get("/programacion/asignatura/lista")
@template(template_file="programacion/programacion_asignatura_lista.pt")
async def programaciones_asignatura_lista(request: Request):
    vm = ProgramacionesAsignaturaViewModel(request)
    await vm.load()

    return vm.to_dict()
