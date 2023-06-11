
import fastapi
import fastapi_chameleon
from starlette.staticfiles import StaticFiles

from views import index
from views import login
from views import principal
from views import usuario
from views import param
from views import asignatura

app = fastapi.FastAPI()


# Método de configuración de routers
def configura_routers():
    # Cargamos la ruta de los archivos estáticos
    app.mount("/static", StaticFiles(directory="static"), name="static")
    # Cargamos los routers
    app.include_router(index.router)
    app.include_router(login.router)
    app.include_router(principal.router)
    app.include_router(usuario.router)
    app.include_router(param.router)
    app.include_router(asignatura.router)


# Método de configuración de templates
def configura_templates():
    fastapi_chameleon.global_init("templates")


# Método de configuración general, que llama a los otros sub-métodos de configuración
def configura():
    configura_routers()
    configura_templates()


# Se configura la aplicación previo a su despliegue
configura()
