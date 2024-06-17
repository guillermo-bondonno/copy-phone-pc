# api/index.py
from flask import Flask, jsonify, render_template, request, redirect, send_from_directory
import logging
from uuid import uuid4
from .db import update_in_db, save_to_db, get_from_db
import os

logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder="../public", template_folder="../templates")

@app.route("/sitemap/<path:path>")
def sitemap(path):
    return app.send_static_file(path)

@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")

@app.route("/")
def index():
    return redirect(f"/transfer?unique_id={str(uuid4())}")

@app.route("/check/<unique_id>")
def check(unique_id):
    data = get_from_db(unique_id)
    return jsonify(data)

@app.route("/transfer")
def transfer():
    #get from query params
    data = request.args.get("data")
    unique_id = request.args.get("unique_id")
    if not unique_id:
        return redirect(f"/transfer?unique_id={str(uuid4())}")
    if not data:
        unique_id = str(uuid4()) if not unique_id else unique_id
        save_to_db(unique_id)
        return render_template("transfer.html", unique_id=unique_id)
    else:
        update_in_db(data, unique_id)
        return render_template("transfer.html", data=data, unique_id=unique_id)

if __name__ == "__main__":
    app.run(debug=True)
