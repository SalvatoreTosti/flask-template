from app import app
from flask import render_template, jsonify, request
from loguru import logger

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/dummy", methods=['POST'])
def dummy():
    string = request.form.get('string')
    return jsonify({"dummy":string})