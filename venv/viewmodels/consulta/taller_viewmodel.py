
from typing import List
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from services import asignatura_service
from services import taller_service
from services import consulta_service
from infrastructure.constants import Mensajes


class ConsultaTallerViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.sigla: str = None
        self.id_taller: int = None
        self.nom_asignatura: str = None
        self.semana: int = None
        self.titulo_preparacion: str = None
        self.detalle_preparacion: str = None

        self.productos: List[dict] = []
        self.consulta: List[dict] = []

    # Función que carga datos y verifica si está conectado al sistema
    async def load(self, sigla, id_taller):
        if self.esta_conectado:
            self.sigla = sigla
            self.id_taller = id_taller
            self.nom_asignatura = await asignatura_service.get_nom_asignatura(self.sigla, self.id_usuario_conectado)
            taller = await taller_service.get_taller(self.request, self.id_taller)
            self.semana = taller["semana"]
            self.titulo_preparacion = taller["titulo_preparacion"]
            self.detalle_preparacion = taller["detalle_preparacion"]
            self.productos = await asignatura_service.get_productos_lista(self.sigla, self.id_taller)

            self.consulta = await consulta_service.get_consulta_taller(self.productos)

        else:
            self.msg_error = Mensajes.ERR_NO_AUTENTICADO.value
