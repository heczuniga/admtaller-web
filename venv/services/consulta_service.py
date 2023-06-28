
from typing import Optional
from typing import List


# Transformamos esta lista de productos en el diccionario que requiere la consulta, es decir, agrupada
async def get_consulta_taller(productos: dict) -> Optional[dict]:
    consulta: List[dict] = []
    items: List[dict] = []
    total: int = 0
    agrupador: str = None

    # Armo al principio la colección vacía [total y tablas, donde tablas es un dict]
    items = []

    # Armamos la colección de salida
    for row in productos:
        if row["cod_agrupador"] == 1:
            agrupador = row["nom_categ_producto"]
        else:
            agrupador = row["nom_agrupador"]

        encontrado = False

        for diccionario in items:
            # Si el agrupador (que es almuerzo personal de servicio o la categoría) está en la lista, agregamos el producto a esa lista, sumamos al subtotal y sumamos al total a esa
            if "agrupador" in diccionario and diccionario["agrupador"] == agrupador:
                diccionario["productos"].append(row)
                diccionario["subtotal"] += row["total"]
                total += row["total"]
                encontrado = True
                break

        # Si el agrupador no está en la lista, agregamos agrupador, agregamos producto, sumamos al subtotal y sumamos al total.
        if not encontrado:
            elemento = {
                "id_agrupador": str(row["cod_agrupador"]) + str(row["cod_categ_producto"]),
                "agrupador": agrupador,
                "subtotal": row["total"],
                "productos": [row],
            }
            items.append(elemento)
            total += row["total"] 

    consulta = {
        "total": total,
        "tablas": items,
    }

    return consulta
