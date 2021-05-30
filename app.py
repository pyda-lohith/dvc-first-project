from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import joblib

params_path= "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        pass
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)