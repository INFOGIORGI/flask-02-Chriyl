from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/") # specifico il path della url
def home() -> str: # funzione che viene richiamata al raggiungimento di http://0.0.0.0:5000/
    nomi = ["christian", "marco", "franco"]
    index = random.randint(0,2)
    return render_template("home.html",titolo="Welcome", nome=nomi[index])

@app.route("/contact")
def contact() -> str:
    return render_template("contact.html")



@app.route("/about")
def about_us() -> str:
    return render_template("about.html")






####################################################
app.run(debug=True) # il debug serve per apportare le modifiche senza re-runnare il server (molto fico non lo sapevo)