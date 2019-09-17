from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/secret")
def secret():
    return "you found the secret"

@app.route("/dwight")
def dwight():
    return "yeooo"

@app.route("/bablo")
def bablo():
    return "sup"

@app.route("/oldironsides")
def oldironsides():
    return "order confirmed!"

@app.route('/results', methods = ["GET", "POST"])
def results():
    userdata = dict(request.form)
    print(userdata['nickname'])
    output = model.shout(userdata['nickname'])
    print(output)
    return return

#hurd da man
