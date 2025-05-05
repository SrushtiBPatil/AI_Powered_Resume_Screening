from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('lr_model.joblib')

@app.route('/')
def home():
    return "Resume Screening Logistic Regression API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])

        # Drop 'job_id' if present
        df = df.drop(columns=['job_id'], errors='ignore')

        prediction = model.predict(df)[0]
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is live"})

