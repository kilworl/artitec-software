from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def template():
    return render_template("form.html")

@app.route('/usuario',methods=['POST'])
def usuario():
    nombreUser = request.form['nombreUser']
    nombreApellido = request.form['nombreApellido']
    Dirreccion = request.form['Dirreccion']
    correo = request.form['correo']
    return "<h1> Bienvenido " + nombreUser + "</h1>" + "<h1><br>" + nombreApellido + "</br></h1>" + "<h1><br>" + Dirreccion + "</br></h1>"+ "<h1><br>" + correo + "</br></h1>"    

if __name__=='__main__':
    app.run(debug=True)