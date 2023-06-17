
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


@router.get("/programacion/eliminar/ano_academ/{ano_academ}/cod_periodo_academ/{cod_periodo_academ}/sigla/{sigla}/seccion/{seccion}")
@template(template_file="programacion/programacion_asignatura_lista.pt")
async def eliminar_asignatura(request: Request, ano_academ: int, cod_periodo_academ: int, sigla: str, seccion: int):
    eliminacion = await programacion_service.delete_programacion_asignatura(request, ano_academ, cod_periodo_academ, sigla, seccion)

    if not eliminacion["eliminado"]:
        vm = ProgramacionesAsignaturaViewModel(request)
        await vm.load()
        vm.msg_error = eliminacion["msg_error"]
        return vm.to_dict()

    # Si no hay errores, se redirecciona a la página principal
    response = fastapi.responses.RedirectResponse("/programacion/asignatura/lista", status_code=status.HTTP_302_FOUND)
    return response


