
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from services import usuario_service


class PasswordViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.nueva_password = ""
        self.confirmacion_nueva_password = ""

    async def validate(self) -> bool:
        valid: bool = True

        if self.nueva_password != self.confirmacion_nueva_password:
            self.msg_error = "La confirmación de la contraseña es incorrecta"
            valid = False

        return valid

    async def update(self):
        # Recuperamos los datos desde el formulario
        form = await self.request.form()
        self.nueva_password = form.get("nueva_password", "")
        self.confirmacion_nueva_password = form.get("confirmacion_nueva_password", "")

        if not await self.validate():
            return

        modificada: bool = await usuario_service.cambio_password(self.request, self.nueva_password, self.confirmacion_nueva_password)
        if not modificada:
            self.msg_error = "Error al cambiar la contraseña"
        else:
            self.msg_exito = "Se ha modificado correctamente la contraseña"
