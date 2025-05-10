from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        contraseña = request.form['password']
        rol = request.form['role']

        if rol == 'paciente':
            return redirect(url_for('paciente'))
        elif rol == 'especialista':
            return redirect(url_for('especialista'))
        else:
            return "Rol no válido", 400

    return render_template('login.html')

@app.route('/paciente')
def paciente():
    return render_template('paciente.html')

@app.route('/carrusel_bandas')
def carrucel():
    return render_template('carrusel_bandas.html')

@app.route('/especialista')
def especialista():
    return render_template('especialista.html')

if __name__ == '__main__':
    app.run(debug=True)
