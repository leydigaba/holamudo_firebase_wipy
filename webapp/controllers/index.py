import web

render = web.template.render("views", base="master")

class Index:
    def GET(self):
        try:
            return render.index()
        except Exception as error:
            message = {
                "Error": str(error)
            }
            print(f"ERROR: {message}")  
            return message


