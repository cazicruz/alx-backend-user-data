#!/usr/bin/env python3
""" a basic flask app"""
from flask import Flask, jsonify


app = Flask(__name__)
app.config["SECRETE_KEY"] = "hardtoguess"

@app.route("/", methods=['GET'], strict_slashs=False)
def index() -> str:
    """Return json respomse
    {"message": "Bienvenue"}
    """
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
