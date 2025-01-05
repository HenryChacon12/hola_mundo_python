from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    nombre = None
    if request.method == 'POST':
        nombre = request.form['nombre']  # Obtener el nombre del formulario
    return render_template('index.html', nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)
