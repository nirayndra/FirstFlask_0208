from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name") or "Anonim"
    lagu = request.form.get("lagu") or "-"
    hobi = request.form.get("hobi") or "-"
    
    return render_template("index.html", name=name, lagu=lagu, hobi=hobi)

if __name__ == "__main__":
    app.run(debug=True)