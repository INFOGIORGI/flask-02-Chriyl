from flask import Flask, render_template
from flask_mysqldb import MySQL
import random
"""
IP: 138.41.20.102
PORTA: 53306
DB: w3schools
USERNAME: ospite
PASSWORD: ospite

"""
app = Flask(__name__)

app.config["MYSQL_HOST"] = "138.41.20.102"
app.config["MYSQL_PORT"] = 53306
app.config["MYSQL_USER"] = "ospite"
app.config["MYSQL_PASSWORD"] = "ospite"
app.config["MYSQL_DB"] = "w3schools"

Mysql= MySQL(app)

@app.route("/") # specifico il path della url
def home() -> str: # funzione che viene richiamata al raggiungimento di http://0.0.0.0:5000/
    nomi = ["christian", "marco", "franco"]
    index = random.randint(0,2)
    return render_template("home.html",titolo="Welcome", nome=nomi[index])

@app.route("/products")
def contact() -> str:
    cursor = Mysql.connect.cursor()
    query = "SELECT * FROM PRODUCTS"
    cursor.execute(query)
    dati: (tuple) = cursor.fetchall()
    
    return render_template("contact.html")



@app.route("/about")
def about_us() -> str:
    return render_template("about.html")






####################################################
app.run(debug=True) # il debug serve per apportare le modifiche senza re-runnare il server (molto fico non lo sapevo)