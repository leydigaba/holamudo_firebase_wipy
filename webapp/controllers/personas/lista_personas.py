import web
from models.personas import Personas  

render = web.template.render("views/personas", base="master")

class ListaPersonas:
    def GET(self):
        try:
            p = Personas() #crea un objecto de personas
            datos = p.lista_personas() #guarda el diccionario en la variable datos
            return render.lista_personas(datos) # renderiza la vista y le manda el diccionario
        except Exception as error:
            message = {
                "Error": str(error)  
            }
            print(f"ERROR: {message}")  
            return message


