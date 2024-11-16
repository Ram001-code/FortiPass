from flask import Flask, render_template, request
import re
import hashlib
import requests

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    common_patterns = ["password", "1234", "abcd", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid using common patterns like 'password' or '1234'.")
    else:
        score += 1

    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("password")
        strength, feedback = check_password_strength(password)
        return render_template("index.html", strength=strength, feedback=feedback, password=password)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)