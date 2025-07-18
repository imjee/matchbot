# web/app.py
from flask import Flask, render_template, request, redirect, session, url_for
import json, os

app = Flask(__name__)
app.secret_key = "matchbot_secret"

DATA_FILE = "data.json"
ADMIN_USERNAME = "hoxibet"
ADMIN_PASSWORD = "hoxibet11"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/admin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == ADMIN_USERNAME and request.form["password"] == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/admin/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("login"))
    users = load_data()
    return render_template("dashboard.html", users=users)

@app.route("/admin/logout")
def logout():
    session.pop("admin", None)
    return redirect("/admin")

def run():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    run()
