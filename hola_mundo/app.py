import web


urls = (
    "/", "Inicio",
    "/saludo", "Saludo"
)

app = web.application(urls, globals())
render = web.template.render("views", base="master")

class Inicio:
    def GET(self):
        return render.inicio()

class Saludo:
    def GET(self):
        return render.saludo()

if __name__ == "__main__":
    app.run()