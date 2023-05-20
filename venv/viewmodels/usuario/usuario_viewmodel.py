
from typing import List
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from services import usuario_service
from services import perfil_service
from services import carrera_service
from infrastructure.constants import Mensajes


class UsuarioViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.id_usuario: str
        self.login: str
        self.apellido_paterno: str
        self.apellido_materno: str
        self.nom: str
        self.nom_preferido: str
        self.cod_perfil: str
        self.cod_carrera: str

        self.usuario: dict
        self.lista_perfil: List[dict]
        self.lista_carrera: List[dict]

    # Función que carga datos y verifica si está conectado al sistema
    async def save(self):
        # Recuperamos los datos desde el formulario
        form = await self.request.form()
        self.id_usuario = int(form.get("id_usuario", "").strip())
        self.login = form.get("login", "").lower().strip()
        self.primer_apellido = form.get("primer-apellido", "").strip()
        self.segundo_apellido = form.get("segundo-apellido", "").strip()
        self.nom = form.get("nom", "").strip()
        self.nom_preferido = form.get("nom-preferido", "").strip()
        self.cod_perfil = int(form.get("cod-perfil", "").strip())
        self.cod_carrera = int(form.get("cod-carrera", "").strip())

        # TODO: Agregar validaciones

        usuario = {
            "id_usuario": self.id_usuario,
            "login": self.login,
            "hash_password": "Holaslashjdkajdh",
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "nom": self.nom,
            "nom_preferido": self.nom_preferido,
            "cod_perfil": self.cod_perfil,
            "cod_carrera": self.cod_carrera,
            "nom_perfil": self.cod_perfil,
            "nom_carrera": self.cod_carrera,
        }
        usuario = await usuario_service.update_usuario(usuario, self.id_usuario)

        if not usuario:
            self.msg_error = "Error al grabar el usuario"
        else:
            self.msg_exito = "Se ha grabado correctamente al usuario"

    async def load(self, id_usuario):
        if self.esta_conectado:
            self.usuario = await usuario_service.get_usuario(id_usuario)
            self.lista_perfil = await perfil_service.get_perfil_lista()
            self.lista_carrera = await carrera_service.get_carrera_lista()
        else:
            self.msg_error = f"{Mensajes.ERR_NO_AUTENTICADO}"
