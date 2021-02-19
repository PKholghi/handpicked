from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form['username'] != 'admin': 
             username = request.form["username"]
             # password = request.form["password"]      
        return render_template("login.html")
        # password = request.form["password"]
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()