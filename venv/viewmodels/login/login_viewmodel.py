
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase

from data.usuario import Usuario
from data.perfil import Perfil
from services import usuario_service


# View model para el login
class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.login = ""
        self.password = ""

    # Rutina que recupera los datos del formulario y realiza validaciones
    async def load(self):

        # Recuperamos los datos desde el formulario
        form = await self.request.form()
        self.login = form.get("login", "").lower().strip()
        self.password = form.get("password", "").lower().strip()

        if not self.login.strip():
            self.msg_error = "Debe ingresar un usuario"

        if not self.password.strip():
            self.msg_error = "Debe ingresar una contraseña"

        # Validamos la autenticación
        usuario: Usuario = usuario_service.autenticacion(self.login, self.password)
        if not usuario:
            self.msg_error = "El usuario y contraseña no son válidos en el sistema"
        else:
            # Ya autenticado, recuperamos el resto de los atributos requeridos para la sesión del usuario
            self.id_usuario = usuario_service.get_id_usuario_by_login(self.login)
            perfil: Perfil = usuario_service.get_perfil(self.id_usuario)
            if not perfil:
                self.msg_error = "No se ha podido determinar un perfil para el usuario"
            self.cod_perfil = perfil.cod_perfil

            ano_academ: int = usuario_service.get_ano_academ(self.id_usuario)
            if not ano_academ:
                self.msg_error = "No se ha podido determinar el año académico vigente"
            self.ano_academ = ano_academ

            nom_carrera: str = usuario_service.get_nom_carrera(self.id_usuario)
            self.nom_carrera = nom_carrera
