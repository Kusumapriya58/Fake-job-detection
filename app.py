# app.py
from flask import Flask, render_template, request, redirect, session
import joblib

app = Flask(_name_)
app.secret_key = "adminlogin123"

# Load ML model
model = joblib.load("fake_job_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# PREDICTION
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    text = request.form['job_text']
    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]
    confidence = model.predict_proba(transformed).max() * 100

    label = "FAKE JOB POST" if prediction == 1 else "REAL JOB POST"

    return render_template("result.html", label=label, confidence=round(confidence, 2))


# ---------------------------------
# ADMIN LOGIN
# ---------------------------------
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form['username'] == "admin" and request.form['password'] == "admin123":
            session['admin'] = True
            return redirect("/dashboard")
        return "Invalid Login!"
    return render_template("admin.html")


# ---------------------------------
# DASHBOARD
# ---------------------------------
@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/admin")

    # Example stats (you can extend this using a database)
    stats = {
        "total_predictions": 240,
        "fake_detected": 83,
        "real_detected": 157
    }
    return render_template("dashboard.html", stats=stats)


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")
    

if _name_ == "_main_":
    app.run(debug=True)