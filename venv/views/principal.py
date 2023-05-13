
import fastapi
from fastapi_chameleon import template
from viewmodels.principal.principal_viewmodel import PrincipalViewModel
from starlette.requests import Request

router = fastapi.APIRouter()


@router.get("/principal")
@template()
def principal(request: Request):
    vm: PrincipalViewModel = PrincipalViewModel(request)
    return vm.to_dict()

