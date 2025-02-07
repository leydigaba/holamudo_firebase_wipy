# holamudo_firebase_wipy

Aquí tienes el texto completado y ajustado:

# Web.py
**HOLA MUNDO DE Web.py**

## 1. Crear un entorno virtual (virtual environment)
```shell
$def with (content)
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gestión de Personas</title>
</head>
<body>
  <!-- Aquí se incluirá el contenido dinámico -->
  $:content
  
  <!-- Navegación -->
  <a href="/index">Volver al inicio</a>
  <a href="/lista_personas">Personas</a>
</body>
</html>

```

## 2. Activar el entorno virtual
### En Linux/MacOS:
```shell
source .venv/bin/activate
```
### En Windows (PowerShell):
```shell
.venv\Scripts\Activate
```

## 3. Desactivar el entorno virtual
```shell
deactivate
```

## 4. Actualizar pip
```shell
pip install --upgrade pip
```

## 5. Instalar entorno de Web.py
Primero, instala Web.py ejecutando:
```shell
pip install web.py
```

## 6. Guardar las dependencias en un archivo de requerimientos
```shell
pip freeze > requirements.txt
```

## 7. Crear la estructura básica de un proyecto Web.py

1. Crea una carpeta llamada `views` para las plantillas HTML.
   ```shell
   mkdir views
   ```

2. Crea un archivo `app.py` con el siguiente código:
   ```python
   import web

   urls = (
       "/", "index"
   )

   app = web.application(urls, globals())
   render = web.template.render("views/")

   class index:
       def GET(self):
           return render.index()

   if __name__ == "__main__":
       app.run()
   ```

3. Dentro de la carpeta `views`, crea un archivo `index.html`:
   ```html
   <!DOCTYPE html>
   <html lang="es">
       <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <title>Hola Mundo con Web.py</title>
       </head>
       <body>
           <h1>¡Hola Mundo desde Web.py!</h1>
       </body>
   </html>
   ```

## 8. Ejecutar el servidor
Corre el proyecto ejecutando:
```shell
python app.py
```

## 9. Abrir en el navegador
Abre tu navegador y visita:  
[http://localhost:8080](http://localhost:8080)

---

## 10. Guardar

```bash
git add .
git commit -m "Primer commit"
git push -u origin main
```