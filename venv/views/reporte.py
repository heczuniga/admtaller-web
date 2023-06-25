
import fastapi
from fastapi_chameleon import template
from viewmodels.reporte.reporte_valorizacion_taller_viewmodel import ReporteValorizacionTaller
from viewmodels.reporte.reporte_presupuesto_estimado_asignatura_viewmodel import ReportePresupuestoEstimadoAsignatura
from viewmodels.reporte.reporte_asignacion_registro_docentes_viewmodel import ReporteAsignacionRegistroDocentes
from starlette.requests import Request

router = fastapi.APIRouter()


@router.get("/reporte/1")
@template(template_file="reporte/valorizacion_taller.pt")
async def reporte_valorizacion_taller(request: Request):
    vm = ReporteValorizacionTaller(request)
    await vm.load()

    return vm.to_dict()


@router.get("/reporte/2")
@template(template_file="reporte/presupuesto_estimado_asignatura.pt")
async def reporte_presupuesto_estimado_asignatura(request: Request):
    vm = ReportePresupuestoEstimadoAsignatura(request)
    await vm.load()

    return vm.to_dict()


@router.get("/reporte/3")
@template(template_file="reporte/asignacion_registro_docentes.pt")
async def reporte_asignacion_registro_deocentes(request: Request):
    vm = ReporteAsignacionRegistroDocentes(request)
    await vm.load()

    return vm.to_dict()
