
from typing import Optional
import httpx
from httpx import Request
from httpx import Response
from infrastructure.constants import APITaller
from infrastructure import cookie_autoriz
from fastapi import status


async def get_programaciones_asignatura_lista(ano_academ: int, id_usuario: int) -> Optional[dict]:

    # Armamos la URL de la API respectiva
    
    url = f"{APITaller.URL_BASE.value}/programacion/asignatura/{ano_academ}/{id_usuario}"

    async with httpx.AsyncClient() as client:
        try:
            response: Response = await client.get(url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise Exception(f"Error en la llamada a la API respectiva. [{str(e)}]")
        except httpx.RequestError as e:
            raise Exception(f"Error de conexión con la API respectiva. [{str(e)}]")

    # Si todo está correcto, Retornamos la respuesta de la API
    agrupadores = response.json()
    return agrupadores


