from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar scaler e modelo
scaler = joblib.load('../models/aquamind_scaler.joblib')
model  = joblib.load('../models/aquamind_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json()
    # Espera JSON com temperature, hour, dayofyear, roll_moist
    df = pd.DataFrame([payload], columns=['temperature','hour','dayofyear','roll_moist'])
    Xs = scaler.transform(df)
    pred = model.predict(Xs)[0]
    return jsonify({'predicted_moisture': round(float(pred), 3)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
