from flask import Flask, render_template, request

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    # Comentario: Renderiza la página principal con información de la empresa ficticia.
    return render_template('index.html')

# Ruta para la página de Quiénes Somos
@app.route('/about')
def about():
    # Comentario: Renderiza la página "Quiénes Somos" con la misión, visión y el equipo.
    return render_template('about.html')

# Ruta para la página de Servicios
@app.route('/services')
def services():
    # Comentario: Renderiza la página "Servicios" mostrando los diferentes servicios ofrecidos.
    return render_template('services.html')

# Ruta para la página de Noticias
@app.route('/news')
def news():
    # Comentario: Renderiza la página de noticias con artículos ficticios.
    return render_template('news.html')

# Ruta para la página de Contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Comentario: Aquí se manejará el envío del formulario de contacto.
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        # Podrías agregar aquí código para manejar los datos recibidos, como enviarlos por correo.
        return f"Gracias, {nombre}. Hemos recibido tu mensaje."
    # Comentario: Si es un GET, simplemente muestra el formulario de contacto.
    return render_template('contact.html')

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
