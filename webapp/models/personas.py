
import pyrebase

config = {
  "apiKey": "AIzaSyB782bGwPNkkqzQFUzEFclWD73b84hj7hA",
  "authDomain": "leydi-53b9f.firebaseapp.com",
  "databaseURL": "https://leydi-53b9f-default-rtdb.firebaseio.com",
  "storageBucket": "leydi-53b9f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Personas:
    def __init__(self):
        pass

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


    def agregar_persona(self, nombre, edad):
        try:
            insertar_personas = {"Nombre": nombre, "Edad": edad}
            self.db.child("personas").push(nueva_persona)
            return {"status": 200, "mensaje": "Persona agregada con éxito"}
        except Exception as e:
            return {"status": 500, "mensaje": f"Error: {str(e)}"}


p = Personas() 
print(p.lista_personas())  
