from flask import Flask, render_template, redirect, url_for, request
#inizializza l'app Flask
app = Flask(__name__)

lista_spesa = []



#rotta principale
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)