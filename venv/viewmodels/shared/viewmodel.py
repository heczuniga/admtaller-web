
from typing import Optional
from starlette.requests import Request


# Se genera el viemodel base que permite recuperar sus datos e información del errore con un simple to_dict()
class ViewModelBase:

    def __init__(self, request: Request):

        # Se aprovecha que al setar el request, FastAPI transforma todo a un diccionario JSON
        self.request: Request = request

        # Para retornar errores
        self.cod_error: Optional[int] = None
        self.error: Optional[str] = None

        # Id del usuario que usa el viewmodel
        self.id_usuario: Optional[int] = None

    # Salida en formato diccionario (JSON)
    def to_dict(self) -> dict:
        return self.__dict__
