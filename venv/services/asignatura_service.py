
from typing import Optional
import httpx
from httpx import Request
from httpx import Response
from infrastructure.constants import APITaller
from infrastructure import cookie_autoriz
from fastapi import status


async def get_asignaturas_lista(id_usuario: int) -> Optional[dict]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE.value}/asignatura/lista/{id_usuario}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    asignaturas = response.json()
    return asignaturas


async def delete_asignatura(request: Request, sigla: str) -> Optional[dict]:

    # Recuperamos el usuario conectado desde la cookie para pasarlo a los servicios como parámetro para segmentar datos
    id_usuario = cookie_autoriz.get_id_usuario_cookie(request)
    error_message: str = None

    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE.value}/asignatura/eliminar/{sigla}/{id_usuario}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.delete(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            error_message = e.response.json().get("detail")
            if "409" not in str(e):
                raise Exception(f"Error en la llamada a la API respectiva. [{error_message}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    eliminacion = response.json()
    return eliminacion


async def get_asignatura(request: Request, sigla: str) -> Optional[dict]:

    # Recuperamos el usuario conectado desde la cookie para pasarlo a los servicios como parámetro para segmentar datos
    id_usuario = cookie_autoriz.get_id_usuario_cookie(request)

    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE.value}/asignatura/{sigla}/{id_usuario}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    asignatura = response.json()
    return asignatura


async def update_asignatura(request: Request, asignatura: dict) -> Optional[dict]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE.value}/asignatura"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.put(url, json=asignatura, follow_redirects=True)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    asignatura = response.json()
    return asignatura


async def insert_asignatura(asignatura: dict) -> Optional[dict]:
    # Armamos la URL de la API respectiva
    url = f"{APITaller.URL_BASE.value}/asignatura"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.post(url, json=asignatura, follow_redirects=True)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:

            if e.response.status_code == status.HTTP_409_CONFLICT:
                return {
                    "msg_error": e.response.json()["detail"],
                    }

            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    asignatura = response.json()
    return asignatura
