import web

urls = (
    "/", "Index",
    "/lista_personas", "ListaPersonas",
    "/personas/list", "GetPersonas"  
)

app = web.application(urls, globals())
render = web.template.render("views", base="master")

class Index:
    def GET(self):
        return render.index()

class ListaPersonas:
    def GET(self):
        try:
            return render.lista_personas()
        except Exception as e:
            return f"Error: {str(e)}"

class GetPersonas:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return web.json.dumps(personas)

if __name__ == "__main__":
    app.run()