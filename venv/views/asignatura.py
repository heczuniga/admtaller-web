
import fastapi
from fastapi_chameleon import template
from viewmodels.asignatura.asignaturas_viewmodel import AsignaturasViewModel
from viewmodels.asignatura.asignatura_viewmodel import AsignaturaViewModel
from starlette.requests import Request
from starlette import status
from services import asignatura_service

router = fastapi.APIRouter()


@router.get("/asignatura/lista")
@template(template_file="asignatura/asignatura_lista.pt")
async def usuario_lista(request: Request):
    vm = AsignaturasViewModel(request)
    await vm.load()

    return vm.to_dict()


@router.get("/asignatura/eliminar/{sigla}")
@template(template_file="asignatura/asignatura_lista.pt")
async def eliminar_asignatura(request: Request, sigla: str):
    eliminacion = await asignatura_service.delete_asignatura(request, sigla)

    if not eliminacion["eliminado"]:
        vm = AsignaturasViewModel(request)
        await vm.load()
        vm.msg_error = eliminacion["msg_error"]

        return vm.to_dict()

    # Si no hay errores, se redirecciona a la página principal
    response = fastapi.responses.RedirectResponse("/asignatura/lista", status_code=status.HTTP_302_FOUND)
    return response


@router.get("/asignatura")
@template(template_file="asignatura/asignatura.pt")
async def asignatura_new(request: Request):
    vm = AsignaturaViewModel(request)
    await vm.load_empty()

    return vm.to_dict()


@router.get("/asignatura/{sigla}")
@template(template_file="asignatura/asignatura.pt")
async def usuario(request: Request, sigla: str):
    vm = AsignaturaViewModel(request)
    await vm.load(sigla=sigla)

    return vm.to_dict()


@router.post("/asignatura/{sigla}")
@template(template_file="asignatura/asignatura.pt")
async def usuario_put(request: Request, sigla: str):
    # Cargamos el view model el cual recupera los datos del formulario respectivo y realiza validaciones
    vm = AsignaturaViewModel(request)
    await vm.update()

    # Si hay errores, recarga el mismo formulario con los datos ingresados
    if vm.msg_error:
        return vm.to_dict()

    # Se carga el formulario con los datos
    await vm.load(sigla=sigla)

    # Se retorna el diccionario entregado por el redirect hacia la página principal
    return vm.to_dict()


@router.post("/asignatura")
@template(template_file="asignatura/asignatura.pt")
async def asignatura_post(request: Request):
    # Cargamos el view model el cual recupera los datos del formulario respectivo y realiza validaciones
    vm = AsignaturaViewModel(request)
    await vm.insert()

    # Si hay errores, recarga el mismo formulario con los datos ingresados
    if vm.msg_error:
        return vm.to_dict()

    # Se carga el formulario con los datos
    await vm.load(sigla=vm.sigla)

    # Se retorna el diccionario entregado por el redirect hacia la página principal
    return vm.to_dict()
