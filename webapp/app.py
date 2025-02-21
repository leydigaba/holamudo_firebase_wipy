import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas
from controllers.personas.insertar_personas import InsertarPersonas as InsertarPersonas



urls = (
    "/", "Index",
    "/ListaPersonas", "ListaPersonas", 
    "/InsertarPersonas", "InsertarPersonas", 
)

app = web.application(urls, globals()) 


def error_handler():
    return web.internalerror("Ocurrió un error en el servidor. Intenta nuevamente.")

if __name__ == "__main__":
    app.run()
