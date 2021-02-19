from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # req = request.form
        # username = req["username"]
        # password = request.form["password"]
        return render_template("login.html")

if __name__ == '__main__':
    app.run()