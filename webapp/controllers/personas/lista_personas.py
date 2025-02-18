import web
from models.personas import Personas  

render = web.template.render("views/personas", base="master")

class ListaPersonas:
    def GET(self):
        try:
            p = Personas() 
            datos = p.lista_personas()
            
            #print(p.lista_personas())  

            return render.lista_personas(datos)
        except Exception as error:
            message = {
                "Error": str(error)  
            }
            print(f"ERROR: {message}")  
            return message


    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            return {
                "status": 200,
                "mensaje": "Todo bien",
                "personas": dict(personas.val()) if personas.val() else {}
            }
        except Exception as e:
            return {
                "status": 500,
                "mensaje": f"Error: {str(e)}",
                "personas": {}
            }