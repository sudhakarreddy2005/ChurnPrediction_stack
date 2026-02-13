# from flask import Flask, request, jsonify
# import joblib
# import json
# import pandas as pd
# import os

# app = Flask(__name__)

# # ------------------------------------
# # LOAD ARTIFACTS
# # ------------------------------------
# model = joblib.load("../models/stack_model.joblib")

# with open("../models/threshold.json") as f:
#     threshold = json.load(f)["threshold"]

# with open("../models/feature_schema.json") as f:
#     feature_schema = json.load(f)

# # ------------------------------------
# # ROUTES
# # ------------------------------------
# @app.route("/")
# def home():
#     return "HR Churn API is running successfully!"

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.json

#     input_df = pd.DataFrame([data])
#     input_df = input_df.reindex(columns=feature_schema)

#     probability = model.predict_proba(input_df)[0][1]
#     prediction = probability >= threshold

#     return jsonify({
#         "churn_probability": round(float(probability), 4),
#         "prediction": "High Risk" if prediction else "Low Risk",
#         "threshold_used": threshold
#     })

# # ------------------------------------
# # RUN
# # ------------------------------------
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))
#     app.run(host="0.0.0.0", port=port)



import os
import json
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# --------------------------------------------------
# INIT APP
# --------------------------------------------------
app = Flask(__name__)

# --------------------------------------------------
# LOAD MODEL & THRESHOLD
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "stack_model.joblib")
THRESHOLD_PATH = os.path.join(BASE_DIR, "..", "models", "threshold.json")

model = joblib.load(MODEL_PATH)

with open(THRESHOLD_PATH) as f:
    threshold = json.load(f)["threshold"]

print("✅ Model Loaded Successfully")
print("✅ Threshold:", threshold)

# --------------------------------------------------
# HEALTH CHECK ROUTE
# --------------------------------------------------
@app.route("/")
def home():
    return jsonify({
        "status": " Churn API Running",
        "model": "Stacked Model",
        "threshold": threshold
    })

# --------------------------------------------------
# PREDICTION ROUTE
# --------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        # Convert JSON → DataFrame
        df = pd.DataFrame([data])

        # Predict probability
        probability = model.predict_proba(df)[0][1]
        prediction = int(probability >= threshold)

        risk_label = "High Risk" if prediction == 1 else "Low Risk"

        return jsonify({
            "churn_probability": round(float(probability), 4),
            "prediction": risk_label,
            "threshold_used": threshold
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


# --------------------------------------------------
# RUN APP
# --------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
