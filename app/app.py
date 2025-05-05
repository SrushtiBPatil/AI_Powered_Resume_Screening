from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("xgb_fraud_detector.pkl")

@app.route('/')
def home():
    return jsonify({"message": "Resume Matcher Fraud Detection API is running 🚀"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expecting a JSON payload
        data = request.get_json()
        df = pd.DataFrame([data])  # Wrap in list to convert dict to DataFrame
        prediction = model.predict(df)
        result = 'Fraudulent' if prediction[0] == 1 else 'Legit'
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
