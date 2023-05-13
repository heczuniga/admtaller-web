
from typing import Optional


class Usuario:
    def __init__(self, id_usuario: int, login: str, hash_password: str, primer_apellido: str, segundo_apellido: str, nom: str, nom_preferido: Optional[str]):
        self.id_usuario: int = id_usuario
        self.login: str = login
        self.hash_password: str = hash_password
        self.primer_apellido: str = primer_apellido
        self.segundo_apellido: str = segundo_apellido
        self.nom: str = nom
        self.nom_preferido: Optional[str] = nom_preferido
