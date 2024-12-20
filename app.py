from flask import Flask, render_template 
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('hola.html')
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
@app.route('/redes')
def redes():
    return render_template('redes.html')



if __name__=="__main__":
    app.run(debug=True)
