import joblib
import numpy as np
import pandas as pd

# 1 – Carrega scaler e modelo
scaler = joblib.load('models/aquamind_scaler.joblib')
model  = joblib.load('models/aquamind_model.joblib')

# 2 – Monte um exemplo de entrada
#    Campos: temperature, hour, dayofyear, roll_moist
exemplo = {
    "temperature": 28.4, 
    "hour": 15, 
    "dayofyear": 145, 
    "roll_moist": 32.1
}

# 3 – Converta em DataFrame e escale
df_ex = pd.DataFrame([exemplo])
X_ex = scaler.transform(df_ex)

# 4 – Predição
pred = model.predict(X_ex)[0]
print(f"Predicted soil moisture: {pred:.2f}%")
# 5 – Converta para JSON