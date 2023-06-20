
import fastapi
from fastapi_chameleon import template
from viewmodels.producto.productos_viewmodel import ProductosViewModel
from viewmodels.producto.producto_viewmodel import ProductoViewModel
from starlette.requests import Request
from starlette import status
from services import producto_service
from infrastructure import cookie_autoriz

router = fastapi.APIRouter()


@router.get("/producto/lista")
@template(template_file="producto/producto_lista.pt")
async def usuario_lista(request: Request):
    vm = ProductosViewModel(request)
    await vm.load()

    return vm.to_dict()


@router.get("/producto/eliminar/{id_producto}")
@template(template_file="producto/producto_lista.pt")
async def eliminar_producto(request: Request, id_producto: int):
    id_usuario = cookie_autoriz.get_id_usuario_cookie(request)
    eliminacion = await producto_service.delete_producto(request, id_producto, id_usuario)

    if not eliminacion["eliminado"]:
        vm = ProductosViewModel(request)
        await vm.load()
        vm.msg_error = eliminacion["msg_error"]

        return vm.to_dict()

    # Si no hay errores, se redirecciona a la página principal
    response = fastapi.responses.RedirectResponse("/producto/lista", status_code=status.HTTP_302_FOUND)
    return response


@router.get("/producto/{id_producto}")
@template(template_file="producto/producto.pt")
async def usuario(request: Request, id_producto: int):
    vm = ProductoViewModel(request)
    await vm.load(id_producto=id_producto)

    return vm.to_dict()
