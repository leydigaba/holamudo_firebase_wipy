import web

render = web.template.render("views/personas", base="master")

class InsertarPersonas:
    def GET(self):
        return render.insertar_personas()
    
    def POST(self):
       
        try:
            f = web.input()
            if f.nombre and f.edad:
                db.child("personas").push({"nombre": f.nombre, "edad": f.edad})
        except Exception as error:
            message = {
                "Error": str(error)
            }
            print(f"ERROR: {message}")  
            return message


        