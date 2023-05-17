
from typing import Optional
import httpx
from httpx import Response
from infrastructure.constants import APITaller


async def get_id_usuario_by_login(login: str) -> Optional[int]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE}/usuario/login/{login}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    id_usuario: int = response.json()["id_usuario"]
    return id_usuario


async def autenticacion(login: str, password: str) -> Optional[dict]:
    autenticacion = {
        "login": login,
        "password": password,
        "autenticado": False,
    }

    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE}/autenticacion"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.post(url, json=autenticacion, follow_redirects=True)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    autenticacion = response.json()
    return autenticacion


async def get_perfil(id_usuario: int) -> Optional[dict]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE}/perfil/usuario/{id_usuario}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    perfil = response.json()
    return perfil


async def get_ano_academ() -> Optional[int]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE}/param/ano_academ/valor"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    ano_academ: int = response.json()["ano_academ"]
    return ano_academ


async def get_nom_carrera(id_usuario: int) -> Optional[str]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE}/perfil/nom_carrera/{id_usuario}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    nom_carrera: str = response.json()["nom_carrera"]
    if not nom_carrera:
        return ""
    return nom_carrera.strip()
