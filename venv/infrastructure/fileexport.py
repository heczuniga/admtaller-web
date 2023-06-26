
import pandas as pd
import io
from fpdf import FPDF
import math


async def generar_excel(datos):
    # Crear un DataFrame desde los datos
    df = pd.DataFrame(datos)

    # Convertir el DataFrame a un archivo Excel
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    return excel_file.getvalue()


async def generar_pdf(datos, filename):
    # Crear el objeto PDF
    pdf = FPDF(orientation='L')

    # Configurar el tamaño de página en landscape
    pdf.set_auto_page_break(auto=False, margin=0)

    # Establecer la fuente y el tamaño del texto
    pdf.set_font("Arial", size=12)

    # Recorrer la lista de datos y agregar cada elemento en una línea separada
    indice = 0
    K_REGISTROS_PAGINA = 16
    for item in datos:
        texto = ""

        if indice % K_REGISTROS_PAGINA == 0:
            # Agregar una página
            pdf.add_page()

            # Título del reporte
            pdf.set_font("Arial", style="B", size=16)
            texto += f"{filename.upper()}"
            pdf.cell(40, 10, txt=texto, ln=True)
            texto = ""

            # Encabezado del reporte
            for clave, valor in item.items():
                texto += f"{clave}\t\t"

            # Establecer la fuente y el tamaño del texto
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(40, 10, txt=texto, ln=True)
            pdf.set_font("Arial", size=12)
            texto = ""

        # Datos del reporte
        for clave, valor in item.items():
            texto += f"{valor}\t\t"
        pdf.cell(0, 10, txt=texto, ln=True)

        indice += 1

    # Guardar el archivo PDF en un archivo temporal
    pdf.output(filename)

    # Leer el contenido del archivo
    with open(filename, "rb") as file:
        pdf_content = file.read()

    return pdf_content
