from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/abolfazl")
def sis():
    return render_template("samanhe.html")








app.run()