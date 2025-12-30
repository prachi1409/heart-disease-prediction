from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# load model (make sure model.pkl is in same folder as this main.py)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Explicitly read each field by name to avoid any ordering issues
        age = float(request.form.get("age", 0))
        sex = float(request.form.get("sex", 0))
        cp = float(request.form.get("cp", 0))
        trestbps = float(request.form.get("trestbps", 0))
        chol = float(request.form.get("chol", 0))
        fbs = float(request.form.get("fbs", 0))
        restecg = float(request.form.get("restecg", 0))
        thalach = float(request.form.get("thalach", 0))
        exang = float(request.form.get("exang", 0))
        oldpeak = float(request.form.get("oldpeak", 0))
        slope = float(request.form.get("slope", 0))
        ca = float(request.form.get("ca", 0))
        thal = float(request.form.get("thal", 0))

        final_data = np.array([[age, sex, cp, trestbps, chol,
                                fbs, restecg, thalach, exang,
                                oldpeak, slope, ca, thal]])
        prediction = model.predict(final_data)[0]

        result = "❤️ Heart Disease Detected" if int(prediction) == 1 else "✔ No Heart Disease"
        return jsonify(result=result)

    except Exception as e:
        # Return error as JSON so front-end can show it
        return jsonify(result=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
