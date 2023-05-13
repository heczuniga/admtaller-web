
from typing import List
from data.dashboard import Resumen
from data.dashboard import Dashboard


def get_dashboard(id_usuario: int) -> List[Dashboard]:
    
    nc: str = None    
    d: List[Dashboard] = []
    r: List[Resumen] = []

    if id_usuario == 1:    
        nc = "Gastronomía"
        r = [
                {
                    "concepto": "Cantidad de asignaturas",
                    "valor": 11,
                },
                {
                    "concepto": "Cantidad de talleres",
                    "valor": 138,
                },
                {
                    "concepto": "Cantidad de productos",
                    "valor": 1798,
                },
                {
                    "concepto": "Cantidad de docentes",
                    "valor": 16,
                },
        ]             
        d.append(Dashboard(nc, r))

        nc = "Administración hotelera"
        r = [
                {
                    "concepto": "Cantidad de asignaturas",
                    "valor": 5,
                },
                {
                    "concepto": "Cantidad de talleres",
                    "valor": 64,
                },
                {
                    "concepto": "Cantidad de productos",
                    "valor": 1187,
                },
                {
                    "concepto": "Cantidad de docentes",
                    "valor": 3,
                },
        ]             
        d.append(Dashboard(nc, r))
    
    if id_usuario == 2:
        nc = "Gastronomía"
        r = [
                {
                    "concepto": "Cantidad de asignaturas",
                    "valor": 11,
                },
                {
                    "concepto": "Cantidad de talleres",
                    "valor": 138,
                },
                {
                    "concepto": "Cantidad de productos",
                    "valor": 1798,
                },
                {
                    "concepto": "Cantidad de docentes",
                    "valor": 16,
                },
        ]             
        d.append(Dashboard(nc, r))

    if id_usuario == 3:
        nc = "Gastronomía"
        r = [
                {
                    "concepto": "Cantidad de talleres asignados",
                    "valor": 4,
                },
        ]             
        d.append(Dashboard(nc, r))

    return d