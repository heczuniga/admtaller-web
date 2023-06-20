
from typing import List
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from services import param_service
from services import producto_service
from services import carrera_service
from services import perfil_service
from services import usuario_service
from infrastructure.constants import Mensajes
from infrastructure.hash import hash_text


class ProductoViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.producto: dict
        self.lista_unidad_medida: List[dict]
        self.lista_categoria_producto: List[dict]

    async def validate(self) -> bool:
        result: bool = True

        return result

    # Función que permite visualizar un formulario para registros nuevos en el sistema
    async def load_empty(self):
        K_NUEVOUSUARIO: int = 0
        if self.esta_conectado:
            self.usuario = await usuario_service.get_usuario(self.request, K_NUEVOUSUARIO)
            self.lista_perfil = await perfil_service.get_perfil_lista(self.request, self.id_usuario_conectado)
            self.lista_carrera = await carrera_service.get_carrera_lista(self.request, self.id_usuario_conectado)
        else:
            self.msg_error = Mensajes.ERR_NO_AUTENTICADO.value

    # Función que carga datos y verifica si está conectado al sistema
    async def update(self):
        # Recuperamos los datos desde el formulario
        form = await self.request.form()
        self.id_usuario = int(form.get("id-usuario", "").strip())
        self.hash_password = form.get("password", "")
        self.login = form.get("login", "").lower().strip()
        self.primer_apellido = form.get("primer-apellido", "").strip()
        self.segundo_apellido = form.get("segundo-apellido", "").strip()
        self.nom = form.get("nom", "").strip()
        self.nom_preferido = form.get("nom-preferido", "").strip()
        self.cod_perfil = int(form.get("cod-perfil", "").strip())
        self.cod_carrera = int(form.get("cod-carrera", "").strip())

        self.usuario = {
            "id_usuario": self.id_usuario,
            "login": self.login,
            "hash_password": self.hash_password,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "nom": self.nom,
            "nom_preferido": self.nom_preferido,
            "cod_perfil": self.cod_perfil,
            "cod_carrera": self.cod_carrera,
            "nom_perfil": "",
            "nom_carrera": "",
        }
        self.lista_perfil = await perfil_service.get_perfil_lista(self.request, self.id_usuario_conectado)
        self.lista_carrera = await carrera_service.get_carrera_lista(self.request, self.id_usuario_conectado)

        if await self.validate():
            # Encriptamos la password antes de pasarla al servicio
            self.hash_password = hash_text(self.hash_password)
            self.usuario["hash_password"] = self.hash_password

            self.usuario = await usuario_service.update_usuario(self.request, self.usuario)

            if not self.usuario:
                self.msg_error = "Error al modificar el usuario"
            else:
                self.msg_exito = "Se ha modificado correctamente al usuario"

    # Función que carga datos y verifica si está conectado al sistema
    async def insert(self):
        # Recuperamos los datos desde el formulario
        form = await self.request.form()
        self.login = form.get("login", "").lower().strip()
        self.hash_password = form.get("password", "").lower().strip()
        self.primer_apellido = form.get("primer-apellido", "").strip()
        self.segundo_apellido = form.get("segundo-apellido", "").strip()
        self.nom = form.get("nom", "").strip()
        self.nom_preferido = form.get("nom-preferido", "").strip()
        self.cod_perfil = int(form.get("cod-perfil", "").strip())
        self.cod_carrera = int(form.get("cod-carrera", "").strip())

        self.usuario = {
            "id_usuario": 0,
            "login": self.login,
            "hash_password": self.hash_password,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "nom": self.nom,
            "nom_preferido": self.nom_preferido,
            "cod_perfil": self.cod_perfil,
            "cod_carrera": self.cod_carrera,
        }
        self.lista_perfil = await perfil_service.get_perfil_lista(self.request, self.id_usuario_conectado)
        self.lista_carrera = await carrera_service.get_carrera_lista(self.request, self.id_usuario_conectado)

        if await self.validate():
            # Encriptamos la password antes de pasarla al servicio
            self.hash_password = hash_text(self.hash_password)
            self.usuario["hash_password"] = self.hash_password

            self.usuario = await usuario_service.insert_usuario(self.usuario)

            if not self.usuario:
                self.msg_error = "Error al agregar el usuario"
            else:
                self.id_usuario = self.usuario["id_usuario"]
                self.msg_exito = "Se ha agregado correctamente al usuario"

    async def load(self, id_producto):
        if self.esta_conectado:
            self.producto = await producto_service.get_producto(self.request, id_producto)
            self.lista_unidad_medida = await param_service.get_unidad_medida_lista(self.request)
            self.lista_categoria_producto = await param_service.get_categoria_producto_lista(self.request)
        else:
            self.msg_error = Mensajes.ERR_NO_AUTENTICADO.value
