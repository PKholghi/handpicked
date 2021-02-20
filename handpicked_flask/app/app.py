from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form["username"]
    return "Welcome " + username +"!"

@app.route('/contact-us', methods=["GET", "POST"])
def contact_us():
    email = request.form["email"]
    return "Thank you for getting in touch! We'll get back to you soon at " + email


if __name__ == '__main__':
    app.run()