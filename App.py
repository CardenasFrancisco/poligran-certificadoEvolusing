from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Puedes enviar aquí los datos del documento también
    return render_template('index.html')

@app.route('/descargar')
def descargar():
    return send_from_directory('static', 'documento.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
