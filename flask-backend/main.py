import flask
from flask import render_template

app = flask.Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html",token="Flask and React")

app.run(debug=True)