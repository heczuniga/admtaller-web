
from typing import List
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from services import principal_service
from data.dashboard import Dashboard


class PrincipalViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.dashboard: List[Dashboard] = principal_service.get_dashboard(self.id_usuario)
