
import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/login/")
@template()
def login():
    return {

    }


@router.get("/logout/")
def index():
    return {
    }
